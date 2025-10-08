class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        ans = []
        count = 0
        n = len(nums)
        if k == 1:
            return nums[:] 
        for i in range(1,k):
            if nums[i] - nums[i-1] != 1:
                count += 1
        
        for i in range(k, n + 1):
            if count == 0:
                ans.append(nums[i-1])
            else:
                ans.append(-1)

            
            if i < n:
                if nums[i-k+1] - nums[i-k] != 1:
                    count -= 1
                if nums[i] - nums[i-1] != 1:
                    count  += 1
        return ans