
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n == 0:
            return 0

        # dp states
        hold = -prices[0]          # buy on day 0
        cash = 0                   # no stock on day 0

        for i in range(1, n):
            # either keep holding, or buy today (cash - prices[i])
            hold = max(hold, cash - prices[i])
            # either keep cash, or sell today (hold + prices[i] - fee)
            cash = max(cash, hold + prices[i] - fee)

        return cash
