class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        store = {}

        def dp(i, buy):
            if i >= len(prices):
                return 0
            if (i, buy) in store:
                return store[(i, buy)]
            
            if buy:
                dont = dp(i+1, buy) 
                buying = dp(i+1, not buy) - prices[i]

                store[(i, buy)] = max(dont, buying)
            else:
                dont = dp(i+1, buy)
                sell = dp(i+1, not buy) + prices[i]

                store[(i, buy)] = max(dont, sell)
            return store[(i, buy)]
        return dp(0, True)