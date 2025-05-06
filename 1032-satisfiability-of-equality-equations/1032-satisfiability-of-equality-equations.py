class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {}
        def find(node):
            if node not in parent:
                parent[node] = node
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        def union(n1, n2):
            parent[find(n1)] = find(n2)
        diff = defaultdict(str)
        for e in equations:
            if e[1:3] == "==":
                union(e[0], e[3])
        for e in equations:
            if e[1:3] == "!=":
                if find(e[0]) == find(e[3]):
                    return False

        
        return True