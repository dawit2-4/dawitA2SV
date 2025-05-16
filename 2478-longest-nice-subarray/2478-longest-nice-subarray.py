class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        length = 0
        i = 0
        while i < (len(nums)):
            used = nums[i]
            j = i + 1
            while j < len(nums) and (used & nums[j]) == 0:
                used |= nums[j]
                j += 1
            length = max(length, j - i)
            i += 1

        return length
