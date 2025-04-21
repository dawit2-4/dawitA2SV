class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        radius = 0
        for house in houses:
            i = bisect.bisect_left(heaters, house)
            dist1 = dist2 = float('inf')
            if i > 0:
                dist1 = abs(house - heaters[i-1])
            if i < len(heaters):
                dist2 = abs(house  - heaters[i])
            
            radius = max(radius, min(dist1, dist2))
        return radius