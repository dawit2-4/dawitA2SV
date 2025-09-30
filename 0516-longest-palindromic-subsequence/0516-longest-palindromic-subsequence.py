class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        
        for d in range(1,len(s)):
            for l in range(len(s) - d):
                r = l + d
                if s[l] == s[r]:
                    dp[l][r] = dp[l+1][r-1] + 2
                else:
                    dp[l][r] = max(dp[l+1][r], dp[l][r-1])
        return dp[0][len(s)-1]