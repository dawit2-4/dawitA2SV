class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = {}
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        def dp(r,c):
            if r ==rows  or c == cols:
                return 0
            if r == rows-1 and c == cols-1:
                if obstacleGrid[r][c] == 0:
                    return 1
                return 0
            if obstacleGrid[r][c] == 1:
                return 0

            if (r,c) in memo:
                return memo[(r,c)]
            
            down = dp(r+1,c)
            right = dp(r,c+1)

            memo[(r,c)] = down + right
            return memo[(r,c)]
        return dp(0,0)