class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def power4(n):
            if n == 1:
                return True
            if n < 4 or n % 4 != 0:
                return False
            return power4(n // 4)
        
        return power4(n)
