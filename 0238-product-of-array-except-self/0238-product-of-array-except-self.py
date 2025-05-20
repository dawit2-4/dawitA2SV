class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * (len(nums) + 1)
        suffix = [1] * (len(nums) + 1)

        for i in range(1,len(prefix)):
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(len(suffix)-2,-1,-1):
            suffix[i] = suffix[i+1] * nums[i]
        ans = []
        for i in range(1, len(suffix)):
            ans.append(suffix[i] * prefix[i-1])
        return ans