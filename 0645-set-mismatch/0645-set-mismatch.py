class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        ans = []

        while i < len(nums):
            correct_pos = nums[i] - 1
            if correct_pos != i:
                if nums[correct_pos] == nums[i]:
                    if nums[i] not in ans:
                        ans.append(nums[i])
                    i += 1
                else: 
                    nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] - 1 != i:
                ans.append(i + 1)
                break
        return ans