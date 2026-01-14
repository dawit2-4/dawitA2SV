class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray = -float('inf')

        max_sum = 0
        for i in range(len(nums)):
            max_sum += nums[i]
            max_subarray = max(max_subarray, max_sum)
            if max_sum < 0:
                max_sum = 0
        return max_subarray
