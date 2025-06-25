class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        minV = -1
        maxV = -1
        invalid = -1
        count = 0

        for i in range(len(nums)):
            if nums[i] == minK:
                minV = i
            if nums[i] == maxK:
                maxV = i
            
            if nums[i] > maxK or nums[i] < minK:
                invalid = i
            
            if maxV != -1 and minV != -1:
                count += max(0,min(maxV, minV) - invalid)
        return count
