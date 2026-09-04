class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def dp(r, c):
            if r == m - 1 and c == n - 1:
                return 1
            if r >= m or c >= n:
                return 0
            if (r,c) in memo:
                return memo[(r,c)]
            
            bottom = dp(r+1, c)
            left = dp(r, c +1)

            memo[(r,c)] = bottom + left
            return memo[(r,c)]
        return dp(0,0)
            
        