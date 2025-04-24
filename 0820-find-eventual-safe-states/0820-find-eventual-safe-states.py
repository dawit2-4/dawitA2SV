class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                adj[graph[i][j]].append(i)
        


        queue = deque()
        ans = []
        for i in range(len(graph)):
            if len(graph[i]) == 0:
                queue.append(i)


        graph1 = []
        for i in range(len(graph)):
            graph1.append(len(graph[i]))
        


        while queue:
            num = queue.popleft()
            ans.append(num)
            for child in adj[num]:
                graph1[child] -= 1
                if graph1[child] == 0:
                    queue.append(child)
            
        return sorted(ans)
