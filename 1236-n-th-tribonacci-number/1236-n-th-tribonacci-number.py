class Solution:
    def tribonacci(self, n: int) -> int:
        store = [float('inf')] * (n + 1)
        def  dp(i):
            if i == 0:
                return 0
            if i == 1 or i == 2:
                return 1
            if store[i] != float('inf'):
                return store[i]
            
            ans = dp(i - 1)  + dp(i- 2) + dp(i - 3)
            store[i] = ans
            return ans
        return dp(n)