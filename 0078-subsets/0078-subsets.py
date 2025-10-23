class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(i, arr):
            if i == len(nums):
                ans.append(arr[:])
                return

            arr.append(nums[i])
            backtrack(i+1, arr)
            arr.pop()
            backtrack(i+1, arr)
        backtrack(0, [])
        return ans
