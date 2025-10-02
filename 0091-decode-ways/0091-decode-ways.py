class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def dp(i):
            if i >= len(s):
                return 1
            if s[i] == '0':
                return 0
            if i in memo:
                return memo[i]
            
            take = dp(i+1)
            if i+1 < len(s) and int(s[i]+s[i+1]) <= 26:
                twoTake = dp(i+2)
                take += twoTake
            memo[i] = take
            return take
        return dp(0)