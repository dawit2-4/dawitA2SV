class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []

        def backtrack(options,path):
            if len(path) == n:
                ans.append("".join(path))
                return

            for opt in options:
                path.append(str(opt))
                if opt == 0:
                    backtrack([1],path)
                else:
                    backtrack([1,0], path)
                path.pop()
        backtrack([1,0],[])
        return ans
