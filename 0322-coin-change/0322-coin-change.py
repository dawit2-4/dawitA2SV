class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        store = [-1] * (amount + 1)

        def dp(remaining):
            if remaining == 0:
                return 0
            if remaining < 0:
                return float('inf')
            if store[remaining] != -1:
                return store[remaining]
            
            min_coins = float('inf')
            for coin in coins:
                min_coins = min(min_coins, dp(remaining - coin)+1)
            store[remaining] = min_coins
            return min_coins
        ans = dp(amount)
        return -1 if ans == float('inf') else ans
        