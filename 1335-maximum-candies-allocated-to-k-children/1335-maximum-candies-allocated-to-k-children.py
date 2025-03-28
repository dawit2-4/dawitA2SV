class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def checker(candy):
            count = 0
            for c in candies:
                count += (c // candy)
                if count >= k:
                    return True
            return False
        
        low = 1 
        high = max(candies)

        while low <= high:
            mid = (low+high)//2
            if checker(mid):
                low = mid + 1
            else:
                high = mid - 1
        return high