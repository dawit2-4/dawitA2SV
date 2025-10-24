class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        city1 = city2 = 0
        costs = sorted(costs, key=lambda x:x[0] - x[1])
        for i in range(len(costs)):
            if i < len(costs) // 2:
                city1 += costs[i][0]
            else:
                city2 += costs[i][1]
        return city1 + city2
