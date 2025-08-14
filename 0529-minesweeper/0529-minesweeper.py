class Solution:
    direction = ((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1))
    def inbound(self, r, c, board):
            return 0<=r<len(board) and 0<=c<len(board[0])
    def Mnumbers(self, board, r, c):
        numberMine = 0
        for dr, dc in self.direction:
            nr, nc = dr + r, dc + c
            if self.inbound(nr, nc, board):
                if board[nr][nc] == "M":
                    numberMine += 1

        return numberMine

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        r,c = click
        if board[r][c] == "M":
            board[r][c] = "X"
        elif board[r][c] == "E":
            mines = self.Mnumbers(board, r, c)
            if mines:
                board[r][c] = str(mines)
            else:
                board[r][c] = "B"
                for dr, dc in self.direction:
                    nr, nc = dr + r, dc + c
                    if self.inbound(nr,nc,board) and board[nr][nc] == "E":
                        self.updateBoard(board, [nr,nc])
        return board
