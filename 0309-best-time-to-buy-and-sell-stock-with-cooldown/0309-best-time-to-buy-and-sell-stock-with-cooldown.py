class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        store = {}

        def dp(i, buy):
            if i >= len(prices):
                return 0
            if (i, buy) in store:
                return store[(i, buy)]
            

            if buy:
                buying = dp(i+1, not buy) - prices[i]
                cool = dp(i+1, buy)
                store[(i, buy)] = max(buying, cool)
            else:
                cool = dp(i+1, buy)
                sell = dp(i+2, not buy) + prices[i]
                store[(i, buy)] = max(sell, cool)
            return store[(i, buy)]
        return dp(0, True)
