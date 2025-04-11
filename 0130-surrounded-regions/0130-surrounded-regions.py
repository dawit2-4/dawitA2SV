class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def inbound(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])

        def dfs(row, col):
            # Mark the 'O' connected to the boundary with a temporary marker
            if not inbound(row, col) or board[row][col] != 'O':
                return
            board[row][col] = 'E' 
            for d in directions:
                new_r = row + d[0]
                new_c = col + d[1]
                dfs(new_r, new_c)
        #step 1 change the "O"s on the boarder to "E"
        for i in range(len(board)):
            for j in [0, len(board[0])-1]:
                if board[i][j] == "O":
                    dfs(i,j)
        for j in range(len(board[0])):
            for i in [0, len(board) -1 ]:
                if board[i][j] == "O":
                    dfs(i,j)
        
        # step 2 change the "O"s that are surrounded in to "X"
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
        # step 3 change the "E"s at the boarder into "O"
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "E":
                    board[i][j] = "O"
    