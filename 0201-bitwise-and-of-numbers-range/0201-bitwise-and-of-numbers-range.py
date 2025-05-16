class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        x = bin(left)[2:]
        y = bin(right)[2:]
        print(x, y)
        ans = ["0"] * len(x)
        if len(y) > len(x):
            return 0
        for i in range(len(x)):
            if x[i] == y[i]:
                ans[i] = x[i]
            else:
                break
        return int("".join(ans), 2)