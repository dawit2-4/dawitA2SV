class Solution:
    def climbStairs(self, n: int) -> int:
        store = [float('inf')] * (n + 1)
        def dp(i):
            if i == 1 or i == 2:
                return i
            if store[i] != float('inf'):
                return store[i]
            ans = dp(i-1) +  dp(i-2)
            store[i] = ans
            return ans
        return dp(n)
