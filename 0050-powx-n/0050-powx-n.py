class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 1:
            return 1
        def helper(x, n):
            if n == 1:
                return x
            if n == 0:
                return 1
            if n < 0:
                return 1/helper(x, abs(n))
                
            if n == 2:
                return x * x
            if n % 2 == 0:
                ans = helper(x, n/2)
                return ans * ans
            else:
                return x * helper(x, n - 1)
        return helper(x,n)