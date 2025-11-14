from math import comb

class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        mod = 10**9 + 7
        difference = endPos - startPos

        # r = number of right moves
        # r = (k + difference) / 2 must be integer
        if (k + difference) % 2 != 0:
            return 0

        r = (k + difference) // 2

        # number of right moves must be valid
        if r < 0 or r > k:
            return 0

        return comb(k, r) % mod
