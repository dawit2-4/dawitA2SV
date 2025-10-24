class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        direction = ((0, 1), (0, -1), (1, 0), (-1, 0))
        def inbound(r, c):
            return 0 <= r < rows and 0 <= c < cols
        visited = set()
        def dfs(r, c):
            if not inbound(r,c):
                return 
            if (r,c) in visited:
                return
            visited.add((r,c))
           
            
            
            for nr, nc in direction:
                nnr = r + nr
                nnc = c + nc

                if inbound(nnr, nnc) and (nnr, nnc) not in visited and grid[nnr][nnc] == '1':
                    dfs(nnr, nnc)
            return
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    count += 1
                    dfs(i,j)
        return count
