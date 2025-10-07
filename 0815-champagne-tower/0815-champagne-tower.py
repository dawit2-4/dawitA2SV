class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        @cache
        def dp(row,col):
            if not row and not col:
                return max((poured-1)/2,0)
            if col == row:
                return max((dp(row-1,col-1)-1)/2,0)
            elif not col:
                return max((dp(row-1,col)-1)/2,0)
            return max((dp(row-1,col-1) + dp(row-1,col) - 1)/2,0)
        if not query_row:
            return 1 if poured>= 1 else poured 
        if not query_glass:
            return min(1, dp(query_row-1,0))
        elif query_glass==query_row:
            return min(1,dp(query_row-1,query_row-1))
        return min(dp(query_row-1,query_glass) + dp(query_row-1,query_glass-1),1)
