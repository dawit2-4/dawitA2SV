class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        ans = 0
        parent = [i for i in range(len(points))]
        for i in range(len(points)):
            for j in range(len(points)):
                if i != j:
                    x, y = points[i]
                    w, z = points[j]

                    dist = abs(x-w) + abs(y-z)
                    edges.append((dist,i,j))
        edges.sort()
        def union(n1, n2):
            parent[find(n1)] = find(n2)
        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        for edge in edges:
            if find(edge[1]) != find(edge[2]):
                union(edge[1],edge[2])
                ans += edge[0]
        return ans

