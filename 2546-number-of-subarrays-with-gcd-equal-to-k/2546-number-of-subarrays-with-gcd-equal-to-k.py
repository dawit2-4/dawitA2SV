class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i, len(nums) + 1):
                if gcd(*nums[i:j]) == k:
                    count += 1
        return count