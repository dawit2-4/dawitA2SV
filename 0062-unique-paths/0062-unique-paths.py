class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        store = {}
        # print(store)
        def inbound(row, col):
            return 0<= row < m and 0<= col < n

        def dp(row,col):
            if not inbound(row, col):
                return 0
            if (row, col) in store:
                return store[(row, col)]
            if row == m - 1 and col == n - 1:
                return 1
        
            #down
            down = dp(row, col+1)
            #right
            right = dp(row+1, col)

            ans = right + down

            store[(row, col)] = ans
            return ans
        return dp(0,0)
        