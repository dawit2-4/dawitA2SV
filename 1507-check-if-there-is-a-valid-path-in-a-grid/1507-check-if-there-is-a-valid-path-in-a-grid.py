class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        rows , cols = len(grid), len(grid[0])
        parent = list(range(rows*cols))
        def find(node):
            if node != parent[node]:
                node = find(parent[node])
            return parent[node]
        def connect_left(row, col):
            if col > 0 and grid[row][col - 1] in (1,4,6):
                current_root = find(row * cols + col)
                left_root = find(row * cols + col-1)
                parent[current_root] = left_root
        def connect_right(row,col):
            if col < cols - 1 and grid[row][col + 1] in (1,3,5):
                current_root = find(row * cols + col)
                right_root = find(row * cols + col+1)
                parent[current_root] = right_root
        def connect_up(row,col):
            if row > 0 and grid[row - 1][col] in (2, 3, 4):
                current_root = find(row * cols + col)
                up_root = find((row-1) * cols + col)
                parent[current_root] = up_root
        def connect_down(row, col):
            if row < rows- 1 and grid[row + 1][col] in (2,5,6):
                current_root = find(row * cols + col)
                down_root = find((row + 1) * cols + col)
                parent[current_root] = down_root
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                node = grid[i][j]

                if node == 1:
                    connect_left(i, j)
                    connect_right(i,j)
                elif node== 2:
                    connect_up(i,j)
                    connect_down(i,j)
                elif node == 3:
                    connect_left(i,j)
                    connect_down(i,j)
                elif node==4:
                    connect_right(i,j)
                    connect_down(i,j)
                elif node==5:
                    connect_left(i,j)
                    connect_up(i,j)
                else:
                    connect_up(i,j)
                    connect_right(i,j)
        start =find(0)
        end = rows * cols - 1
        end = find(end)
        return start ==end
            
