class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        difference = []
        for city1, city2 in costs:
            difference.append([city2 - city1, city1, city2])
        
        difference.sort()
        ans =0
        for i in range(len(difference)):
            if i <len(costs)//2:
                ans += difference[i][2]
            else:
                ans += difference[i][1]
        return ans
