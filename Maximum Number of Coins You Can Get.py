class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        sum = 0
        n = len(piles)//3

        for i in range(n,len(piles),2):
            sum += piles[i]
        
        return sum
