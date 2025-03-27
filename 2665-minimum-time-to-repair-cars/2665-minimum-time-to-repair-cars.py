class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def checker(m):
            total_cars = 0
            for rank in ranks:
                total_cars += math.floor(math.sqrt(m/rank))
            # print(total_cars)
            if total_cars >= cars:
                return True
            else:
                return False
        high = min(ranks) * cars**2
        low = 1

        while low <= high:
            mid = (high+low)//2
            if checker(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low