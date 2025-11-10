class Solution:
    def __init__(self):
        self.mod = ((10**9)+7)
    def countGoodNumbers(self, n: int) -> int:
        odd = self.helper(4, n // 2)
        even = self.helper(5, n - n//2)

        return (odd * even) % self.mod

        

    def helper(self, base, exponent):
        result = 1

        while exponent > 0:
            if exponent & 1:
                result = (result * base) % self.mod
            base = (base * base) % self.mod
            exponent >>= 1
        return result
    
