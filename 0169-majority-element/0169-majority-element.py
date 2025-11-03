class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        for key, val in c.items():
            if val > len(nums) // 2:
                return key
            