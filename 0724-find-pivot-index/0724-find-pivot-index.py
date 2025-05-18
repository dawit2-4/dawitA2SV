from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        pref_l = nums[:]
        pref_r = nums[:]

        
        for i in range(1, n):
            pref_l[i] = pref_l[i - 1] + nums[i]

        
        for i in range(n - 2, -1, -1):
            pref_r[i] = pref_r[i + 1] + nums[i]

        
        for i in range(n):
            left_sum = pref_l[i - 1] if i > 0 else 0
            right_sum = pref_r[i + 1] if i < n - 1 else 0
            if left_sum == right_sum:
                return i

        return -1
