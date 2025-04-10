class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        def inbound(row,col):
            return 0<=row<len(grid) and 0<=col<len(grid[0])

        def dfs(i,j):
            count = 1
            for d in  directions:
                new_r = i + d[0]
                new_c = j + d[1]

                if inbound(new_r, new_c):

                    if grid[new_r][new_c] == 1 and not visited[new_r][new_c]:
                        visited[new_r][new_c] = True
                        count += dfs(new_r, new_c)
                        print(count)
            return count

        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j]:
                    visited[i][j] = True
                    if grid[i][j] == 1:
                        area = dfs(i,j)
                        max_area = max(max_area, area)
                    else:
                        continue
        return max_area