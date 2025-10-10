class Solution:
    def findGCD(self, nums: List[int]) -> int:
        x = min(nums)
        y = max(nums)

        def gcd(x,y):
            if x == 0:
                return y
            else:
                return gcd(y%x, x)
        return gcd(x,y)