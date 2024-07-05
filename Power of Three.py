class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def power3(n):
            if n == 1:
                return True
            if n < 3 or n % 3 != 0:
                return False
            return power3(n // 3)
        return power3(n)
