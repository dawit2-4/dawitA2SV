class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def bfs(i):
            queue = deque()
            queue.append([i,-1])
            visited = defaultdict(int)
            visited[i] = -1

            while queue:
                
                for _ in range(len(queue)):
                    num, color = queue.popleft()
                    new_color = color * -1
                    for child in graph[num]:
                        if child in visited:
                            if visited[child] != new_color:
                                return False
                        else:
                            visited[child] = new_color
                            queue.append([child, new_color])
            return True
        for i in range(len(graph)):
            if bfs(i):
                continue
            else:
                return False
        return True
       
                    