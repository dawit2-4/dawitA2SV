class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        store = {}
        def dp(idx, summ):
            # print(idx, summ)
            if (idx, summ) in store:
                return store[(idx,summ)]
            if idx >= len(nums):
                return 0
            if summ == target and idx == len(nums) - 1:
                return 1
            ans = dp(idx+1, summ+nums[idx]) + dp(idx+1,summ-nums[idx])

            store[(idx, summ)] = ans
            return ans
        return dp(-1, 0)

