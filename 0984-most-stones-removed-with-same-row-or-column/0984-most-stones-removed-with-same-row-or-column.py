class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = [i for i in range(len(stones))]
        def union(n1,n2):
            parent[find(n1)] = find(n2)
        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        
        for i in range(len(stones)):
            for j in range(len(stones)):
                if i != j:
                    if find(i) == find(j):
                        continue
                    if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                        union(i,j)
        x = set(parent)
       
        return len(parent) - len(x)