class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        # path = []

        def backtrack(opening, closing, path):
            print(path[:], opening, closing)
            if opening > closing:
                return
            if opening == n:
                path.append('(')
                backtrack(opening-1, closing, path[:])
                return
            if closing == 0:
                return
            if opening == 0:
                ans.append("".join(path[:] + ([')']*closing)))
                return
            path.append('(')
            backtrack(opening-1,closing,path[:])
            path.pop()
            path.append(')')
            backtrack(opening, closing - 1,path[:])
        backtrack(n,n,[])
        return ans
