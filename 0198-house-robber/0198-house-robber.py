class Solution:
    def rob(self, nums: List[int]) -> int:
        store = {}
        def dp(i):
            if i >= len(nums):
                return 0
            if i in store:
                return store[i]
            
            #take 
            take = nums[i] + dp(i+2)

            #not take
            notTake = dp(i+1)

            store[i] = max(take, notTake)

            return store[i]
        return dp(0)      