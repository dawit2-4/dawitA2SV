class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        store = [[-1] * len(grid[0]) for i in range(len(grid))] 
        def inbound(row, col):
            return 0<= row < len(grid) and 0<= col < len(grid[0])
        def dp(row, col):
            if not inbound(row, col):
                return float('inf')
            if store[row][col] != -1:
                return store[row][col]
            if row == (len(grid) - 1) and col == (len(grid[0]) - 1):
                return grid[row][col]
            
            #down
            down = dp(row+1, col)
            #right
            right = dp(row,  col+1)

            ans = min(down, right) + grid[row][col]
            store[row][col] = ans
            return ans
        
        return dp(0,0)