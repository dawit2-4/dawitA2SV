class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parent = [i for i in range(len(isConnected))]
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        provinces = len(isConnected)

        
        for r in range(len(isConnected)):
            for c in range(len(isConnected)):
                if isConnected[r][c] == 1:
                    parent_r = find(r)
                    parent_c = find(c)
                    if parent_r != parent_c:
                        parent[parent_r] = parent_c
                        provinces -= 1

        return provinces
        