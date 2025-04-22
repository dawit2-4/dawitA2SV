class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for i in range(len(redEdges)):
            graph[redEdges[i][0]].append((redEdges[i][1], 0))
        for i in range(len(blueEdges)):
            graph[blueEdges[i][0]].append((blueEdges[i][1], 1))
        
        visited = set([(0,0),(0,1)])
        queue = deque([(0,0),(0,1)])
        ans = [-1] * n
        level = 0

        
        while queue:
            c = len(queue)
            for _ in range(c):
                node, color = queue.popleft()
                
                if ans[node] == -1:
                    ans[node] = level
                for child in graph[node]:
                    if (child[0], child[1]) not in visited:
                        if child[1] != color:
                            new_c = 1 - color 
                            queue.append((child[0], new_c))
                            visited.add((child[0],new_c))
            level += 1
        return ans

                

