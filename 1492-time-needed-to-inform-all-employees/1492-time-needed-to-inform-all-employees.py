class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        time = 0
        graph = defaultdict(list)

        for i in range(n):
            if manager[i] == -1:
                continue
            graph[manager[i]].append(i)
        def dfs(num):
            if num not in graph:
                return 0
            ans = -float('inf')
            for child in graph[num]:
                ans = max(ans,dfs(child))
            return ans + informTime[num]
        return dfs(headID)
