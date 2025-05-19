class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        if nums[1] + nums[0] <= nums[2]:
            return "none"
        x = set(nums)
        if len(x) == 1:
            return "equilateral"
        elif len(x) == 2:
            return "isosceles"
        else:
            return "scalene"