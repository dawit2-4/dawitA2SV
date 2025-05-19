class Solution:
    def addDigits(self, num: int) -> int:
        num = str(num)
        while len(num) > 1:
            new_n = 0
            for n in num:
                new_n += int(n)
            num = str(new_n)
        return int(num)