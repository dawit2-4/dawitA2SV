class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1 or x == 0:
            return x
        l = 0
        r = x 
        val = 0

        while l <= r:
            mid = (l+r) // 2
            # sq = (mid * mid)
            if mid*mid <= x:
                val = mid
                l = mid + 1
            else:
                r = mid - 1
        return val
        

