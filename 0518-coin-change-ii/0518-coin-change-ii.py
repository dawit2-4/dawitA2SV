class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        store = {}
        def dp(i,summ):
            if summ == amount:
                return 1
            if (i,summ) in store:
                return store[(i,summ)]
            if summ > amount or i == len(coins):
                return 0
            
            take = dp(i, summ + coins[i])
            skip = dp(i+1,summ)
            store[(i,summ)] = take + skip
            return store[(i, summ)]
        return dp(0,0)


        