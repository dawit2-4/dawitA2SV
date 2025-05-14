class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x = 0
        for num in nums:
            x = x ^ num
        y = 0
        for i in range(len(nums)+1):
            y = y ^ i
        return x ^ y