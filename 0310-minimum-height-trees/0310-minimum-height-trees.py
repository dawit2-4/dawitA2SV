class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        leaves = deque([node for node in graph if len(graph[node]) == 1])
        remaining = n

        while remaining > 2:
            leaves_count = len(leaves)
            remaining -= leaves_count

            for _ in range(leaves_count):
                leaf = leaves.popleft()
                child = graph[leaf].pop()
                graph[child].remove(leaf)
                if len(graph[child]) == 1:
                    leaves.append(child)
        return list(leaves)

