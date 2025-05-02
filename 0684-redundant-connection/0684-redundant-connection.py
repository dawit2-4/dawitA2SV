class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        visited = set()
        max_n = 0
        for i, j in edges:
            max_n = max(max_n, max(i,j))
        parent = [i for i in range(max_n +1)]
        size = [1] * (max_n+1)
        def find(n1):
            if n1 == parent[n1]:
                return n1
            parent[n1] = find(parent[n1])
            return parent[n1]
        for n1, n2 in edges:
            # print(parent)
            root1 = find(n1)
            root2 = find(n2)

            if root1 == root2:
                return [n1,n2]
            else:
                if size[root1] >= size[root2]:
                    parent[root2] = root1
                    size[root1] += size[root2]
                else:
                    parent[root1] = root2
                    size[root2] += size[root1]
