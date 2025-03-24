class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        ans = []

        # create a backtarck
        def backtrack():
            if len(path) == len(nums):
                ans.append(path[:])
                return
            
            for x in nums:
                if x not in path:
                    path.append(x)
                    backtrack()
                    path.pop()
                    
        backtrack()  
        return ans