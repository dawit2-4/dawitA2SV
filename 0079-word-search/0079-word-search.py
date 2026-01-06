class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def helper(i, j, visited, idx):
            
            if (i, j) in visited:
                return False
            if board[i][j] != word[idx]:
                return False
            if idx == len(word) - 1:
                return True
            visited.add((i, j))
            
            for dr, dc in direction:
                new_row, new_col = i + dr, j + dc
                if inbound(new_row, new_col):
                    response = helper(new_row, new_col, visited, idx + 1)
                    if response:
                        return True
            visited.remove((i,j))
            return False

        direction = ((1,0), (0,1), (-1,0), (0,-1))
        def inbound(r, c):
            return 0 <= r < len(board) and 0 <= c < len(board[0])
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if helper(i,j,set(), 0):
                        return True
        return False
        
        


            

