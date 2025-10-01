class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        store = {}

        def dp(i):
            if i >= len(cost):
                return 0
            if i in store:
                return store[i]
            
            one = cost[i] + dp(i+1)
            two = cost[i] + dp(i+2)

            store[i] = min(one, two)
            return store[i]
        return min(dp(0), dp(1))
