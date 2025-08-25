class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        board.reverse()
        def helper(z):
            row = math.ceil(z/n) - 1
            x = n * row + 1
            y = x + n - 1
            if row % 2:
                return (row, y - z)
            return (row,z - x)
      
        
        queue = deque([1])
        visited = {1}
        lvl = 0
        while queue:  
            for _ in range(len(queue)):
                num = queue.popleft()
                if num == n*n:
                    return lvl

                for k in range(1,7):
                    curr = min(num + k, n*n)
                    i,j = helper(curr)
                    # print(curr, i,j)
                    if (board[i][j] == -1) and (curr not in visited):
                        queue.append(curr)
                        visited.add(curr)

                    elif board[i][j] != -1:
                        ii,jj = helper(board[i][j])
                        # new_num = board[ii][jj]
                        # print(curr, new_num)
                        if board[i][j] not in visited:
                            queue.append(board[i][j])
                            visited.add(board[i][j])
            lvl += 1

        return -1