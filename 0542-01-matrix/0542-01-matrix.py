from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def inbound(r, c):
            return 0 <= r < len(mat) and 0 <= c < len(mat[0])
        
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        queue = deque()
        visited = [[False] * len(mat[0]) for _ in range(len(mat))]
        res = [[0] * len(mat[0]) for _ in range(len(mat))]


        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 0:
                    queue.append((r, c))
                    visited[r][c] = True


        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if inbound(nr, nc) and not visited[nr][nc]:
                    res[nr][nc] = res[r][c] + 1
                    visited[nr][nc] = True
                    queue.append((nr, nc))

        return res
