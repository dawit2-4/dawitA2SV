class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i, j = 0, int(math.sqrt(c))
        while i <= j:
            calc = (j ** 2) + (i ** 2)
            if calc == c:
                return True
            elif calc < c:
                i += 1
            else:
                j -= 1
        return False
