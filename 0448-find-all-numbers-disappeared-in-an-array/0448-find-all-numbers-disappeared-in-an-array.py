class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        ans = []

        while i < len(nums):
            correct_pos = nums[i] - 1
            if correct_pos != i:
                if nums[correct_pos] == nums[i]:
                    i += 1
                else:
                    nums[correct_pos], nums[i] = nums[i], nums[correct_pos]
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] != i + 1:
                ans.append(i+1)
        return ans