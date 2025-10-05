class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        store = {}

        def dp(row, col):
            if row == len(triangle)-1:
                return triangle[row][col]
            if (row, col) in store:
                return store[(row, col)]
            
            down = dp(row + 1, col) 
            diag = dp(row + 1,  col + 1)

            store[(row, col)] = min(down, diag) + triangle[row][col]
            return store[(row, col)]
        return dp(0,0)