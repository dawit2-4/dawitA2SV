class Solution:
    def make_squares(self, num):
        arr = []
        for i in range(1, num+1):
            x = sqrt(i)
            if x == int(x):
                arr.append(i)
        return arr
    def numSquares(self, n: int) -> int:
        arr = self.make_squares(n)
        store = {}
        # print(arr)

        def dp(remaining):
            if remaining == 0:
                return 0
            if remaining < 0:
                return float('inf')
            if remaining in store:
                return store[remaining]

            min_nums = float('inf')
            for a in arr:
                min_nums = min(min_nums, dp(remaining - a) + 1)
            store[remaining] = min_nums
            return store[remaining]
        return dp(n)