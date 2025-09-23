class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        store = {}

        def dp(i, j):
            if (i,j) in store:
                return store[(i,j)]
            if i == n and j == m:
                return 0
            if i == n:
                return 0
            if j == m:
                return 0
           
            if text1[i] == text2[j]:
                val = 1 + dp(i+1, j+1)
                store[(i,j)] = val
                return val
            if text1[i] != text2[j]:
                val = max(dp(i, j+1),dp(i+1,j))
                store[(i,j)] = val
                return val
            
        return dp(0,0)   

