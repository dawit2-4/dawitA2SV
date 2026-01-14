class Solution:
    def reverse(self, x: int) -> int:
        number_reversed = 0
        original_number = x
        sign = False
        if x < 0:
            sign = True
        x = abs(x)
        
        while x > 0:
            remain = x % 10
            x = x // 10
            number_reversed *= 10
            number_reversed += remain
        if number_reversed > (2 ** 31) - 1 or number_reversed < -(2 ** 31):
            return 0
        if sign:
            return -number_reversed
        return number_reversed