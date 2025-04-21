class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        NegCol = set()
        PosCol = set()

        ans = []
        board = [["."] * n for _ in range(n)]


        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                ans.append(copy)
            
            for c in range(n):
                if c in col or (r - c) in NegCol or (r + c) in PosCol:
                    continue
                
                board[r][c] = "Q"
                col.add(c)
                NegCol.add(r-c)
                PosCol.add(r+c)

                backtrack(r + 1)

                board[r][c] = "."
                col.remove(c)
                NegCol.remove(r-c)
                PosCol.remove(r+c)
        backtrack(0)

        return ans