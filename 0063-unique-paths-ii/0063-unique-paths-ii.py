class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid[0]), len(obstacleGrid)
        dp = [[0] * m for _ in range(n)]

        if obstacleGrid[n-1][m-1] == 1:
            return 0
        dp[n-1][m-1] = 1

        # bottom row
        for j in range(m-2, -1, -1):
            if obstacleGrid[n-1][j] == 1:
                dp[n-1][j] = 0
            else:
                dp[n-1][j] = dp[n-1][j+1]

        # rightmost column
        for i in range(n-2, -1, -1):
            if obstacleGrid[i][m-1] == 1:
                dp[i][m-1] = 0
            else:
                dp[i][m-1] = dp[i+1][m-1]

        # fill rest of grid
        for i in range(n-2, -1, -1):
            for j in range(m-2, -1, -1):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]

        return dp[0][0]
