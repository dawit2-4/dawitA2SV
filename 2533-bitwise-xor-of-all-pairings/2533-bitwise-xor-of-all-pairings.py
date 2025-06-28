class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        x = 0
        y = 0
        for n in nums1:
            x ^= n
        for m in nums2:
            y ^= m
        ans = 0

        if len(nums1) % 2 == 1:
            ans ^= y
        if len(nums2) % 2 == 1:
            ans ^= x

        return ans
                