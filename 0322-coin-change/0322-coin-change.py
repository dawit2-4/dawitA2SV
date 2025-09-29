class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [0] * (amount + 1)

        for i in range(1,amount+1):
            min_coin = float('inf')

            for coin in coins:
                j = i - coin
                if j < 0:
                    break
                min_coin = min(min_coin, 1 + dp[j])
            dp[i] = min_coin
        if dp[amount] != float('inf'):
            return dp[amount]
        return -1
        