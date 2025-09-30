class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for i in range(amount+1):
                remaining = i - coin
                if remaining >= 0:
                    dp[i] += dp[remaining]
        return dp[-1]


        