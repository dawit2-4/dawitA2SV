class Solution:
    def rob(self, nums: List[int]) -> int:
        store = {}
        def dp(i, amount):
            if i >= len(nums):
                return 0
            if (i,amount) in store:
                return store[(i, amount)]
            
            #take 
            take = nums[i] + dp(i+2, amount + nums[i])

            #not take
            notTake = dp(i+1, amount)

            store[(i, amount)] = max(take, notTake)

            return store[(i, amount)]
        return dp(0, 0)      