class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        queue = deque()
        rows = len(board)
        cols = len(board[0])
        visited = set()
        directions = ((1,0),(-1,0),(0,1),(0,-1))
        def inbound(i,j):
            return 0 <= i < rows and 0 <= j < cols


        for i in range(rows):
            if board[i][0] == 'O':
                queue.append((i,0))
                
            if board[i][cols-1] == 'O':
                queue.append((i, cols-1))
        for j in range(cols):
            if board[0][j] == 'O':
                queue.append((0,j))
            if board[rows-1][j] == 'O':
                queue.append((rows-1, j))
        
        while queue:
            n = len(queue)
            for _ in range(n):
                i, j = queue.popleft()
                visited.add((i,j))
                for dx, dy in directions:
                    new_r, new_c = i + dx, j + dy
                    if inbound(new_r, new_c) and board[new_r][new_c] == 'O' and (new_r, new_c) not in visited:
                        queue.append((new_r, new_c))
                        visited.add((new_r, new_c))

        # print(visited)
        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visited and board[i][j] == 'O':
                    board[i][j] = 'X'
        return board