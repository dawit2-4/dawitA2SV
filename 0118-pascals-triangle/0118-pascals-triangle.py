class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1]]
        for i in range(1,numRows):
            add = []
            for j in range(len(dp[i-1]) +1):
                if j - 1 < 0:
                    x = 0
                else:
                    x = dp[i-1][j-1]
                if j > len(dp[i-1]) - 1:
                    y = 0
                else:
                    y = dp[i-1][j]
                add.append(x+y)
            dp.append(add)
        return dp
                