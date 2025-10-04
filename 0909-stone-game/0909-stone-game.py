class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        store = {}
        
        def dp(l, r):
            if l == r:
                return piles[l]
            
            if (l,r) in store:
                return store[(l,r)]
            
            pick_left = piles[l] - dp(l+1, r)
            pick_right = piles[r] - dp(l, r-1)

            store[(l,r)] = max(pick_left, pick_right)
            return store[(l, r)]
        return dp(0, len(piles) - 1) > 0