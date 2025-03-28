class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        
        
        def checker(n):
            last_placed = position[0]
            count = 1
            for i in range(1,len(position)):
                if position[i] - last_placed >= n:
                    last_placed = position[i]
                    count += 1

                    if count == m:
                        return True
            return False
                
        low = 1
        high = position[-1] - position[0]

        while low <= high:
            print(low,high)
            mid = (low+high)//2
            if checker(mid):
                low = mid + 1
            else:
                high = mid - 1
        
        return high