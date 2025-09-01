class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        def backtrack(path, i):
            if i == len(s):
                ans.append("".join(path))
                return
            
            if s[i].isalpha():
                #choose lowercase
                path.append(s[i].lower())
                backtrack(path, i+1)
                path.pop()

                #chooswe upper
                path.append(s[i].upper())
                backtrack(path, i+1)
                path.pop()
            else:
                path.append(s[i])
                backtrack(path, i+1)
                path.pop()
        backtrack([], 0)
        return ans

