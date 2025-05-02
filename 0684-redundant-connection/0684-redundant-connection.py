class UnionFind:
    def __init__(self, n):
        self.size = [1] * (n + 1)
        self.parent = [i for i in range(n+1)]
    def find(self, node):
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node
    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 == root2:
            return [node1, node2] 
        else:
            if self.size[root1] >= self.size[root2]:
                self.parent[root2] = root1
                self.size[root1] += self.size[root2]
            else:
                self.parent[root1] = root2
                self.size[root2] += self.size[root1]





class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:    
        max_n = 0
        for i, j in edges:
            max_n = max(max_n, max(i,j))
        unionfind = UnionFind(max_n)
        for n1, n2 in edges:
            ans = unionfind.union(n1,n2)
            if ans:
                return ans
        