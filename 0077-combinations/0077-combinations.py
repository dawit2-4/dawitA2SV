class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        ans = []

        def backtrack(i):
            if len(path) == k:
                ans.append(path[:])
            
            for j in range(i+1, n+1):
                path.append(j)
                backtrack(j)
                path.pop()
        backtrack(0)
        return ans