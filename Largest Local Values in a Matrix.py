class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = []
        

        for i in range(n - 2):
            row = []
            for j in range(n - 2):
                maxm = max(
                    grid[i][j], grid[i][j+1], grid[i][j+2],
                    grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2],
                    grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2]
                )
                row.append(maxm)
            ans.append(row)
        return ans
