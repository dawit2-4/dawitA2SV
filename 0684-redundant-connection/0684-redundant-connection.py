class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        visited = set()
        max_n = 0
        for i, j in edges:
            max_n = max(max_n, max(i,j))
        parent = [0] * (max_n+1)
        
        for n1, n2 in edges:
            
            if parent[n1] == parent[n2] and parent[n1] != 0:
                return [n1,n2]
            elif parent[n1] == 0 and parent[n2] == 0:
                parent[n1] = n2
                parent[n2] = n2
            else:
                if parent[n1] == 0:
                    parent[n1] = parent[n2]
                elif parent[n2] == 0:
                    parent[n2] = parent[n1]
                else:
                    prev = parent[n1]
                    for i in range(len(parent)):
                        if parent[i] == prev:
                            parent[i] = parent[n2]
                    
        