class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        def in_bound(r,c):
            return 0 <= r < rows and 0 <= c < cols
        dxn = ((0,1), (1, 0),  (0, -1), (-1, 0))
        
        visited = set()
        def dfs(r, c, i):
            if board[r][c] != word[i]:
                return False
            if i == len(word) - 1:
                return True
            visited.add((r,c))
            for row, col in dxn:
                nr, nc = row + r, col + c
                if in_bound(nr,nc) and (nr, nc) not in visited:
                    if dfs(nr, nc, i+1):
                        return True
            visited.remove((r,c))
            return False
        ans = False
        for i in range(rows):
            for j in range(cols):
                    ans |= dfs(i,j,0)
        return ans
            