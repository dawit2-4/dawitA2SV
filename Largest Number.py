class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        ans = ''
        nums.sort()
        for i in range(len(nums) - 1):
            for j in range(i+1,len(nums)):
                if str(nums[i]) + str(nums[j]) < str(nums[j]) + str(nums[i]):
                    nums[i], nums[j] = nums[j], nums[i]
        for i in range(len(nums)):
            ans += str(nums[i])
        return str(int(ans))
