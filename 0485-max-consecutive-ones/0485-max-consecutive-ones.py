class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                max_ones += 1
                nums[i] = max_ones
            else:
                max_ones = 0
        return max(nums)