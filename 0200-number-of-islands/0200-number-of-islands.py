class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def inbound(r,c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        ans = 0

        direction = [(-1,0), (1, 0), (0, -1), (0, 1)]
        visited = set()
        def dfs(r, c):
            visited.add((r, c))
            
            for dx, dy in direction:
                new_r, new_c = r + dx, c + dy
                if (new_r, new_c) not in visited and inbound(new_r, new_c) and grid[new_r][new_c] == "1":
                    dfs(new_r, new_c)
            return 
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in visited and grid[r][c] == "1":
                    ans += 1
                    dfs(r, c)

                    
        return ans