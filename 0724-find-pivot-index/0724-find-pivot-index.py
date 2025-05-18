class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        summ = 0
        n = len(nums)
        total = sum(nums)

        for i in range(n):
            if total - (summ + nums[i]) == summ:
                return i
            else:
                summ += nums[i]
        return -1