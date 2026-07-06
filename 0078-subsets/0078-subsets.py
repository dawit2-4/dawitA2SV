class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
       
        def dp(i, temp):
            nonlocal ans
            if i >= len(nums):
                return
            temp.append(nums[i])
            ans.append(temp[:])
            
            dp(i+1, temp)
            temp.pop()
            dp(i+1, temp)
        dp(0, [])
        return ans
