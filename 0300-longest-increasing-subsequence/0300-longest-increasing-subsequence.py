class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        nums = nums + [inf]
        store = {}
        def rec(end):
            max_val = 1
            if end in store:
                return store[end]
            for i in range(end):
                
                if nums[i] < nums[end]:
                    val = rec(i)
                    max_val = max(1 + val, max_val)
            
            store[end] = max_val
            return max_val
        return rec(len(nums) - 1) - 1