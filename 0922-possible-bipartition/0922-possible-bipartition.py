class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        # Build the graph (1-indexed)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        
        group = {}

        # BFS to assign groups
        for person in range(1, n + 1):
            if person not in group:
                queue = deque([person])
                group[person] = 1
                while queue:
                    current = queue.popleft()
                    for neighbor in graph[current]:
                        if neighbor in group:
                            if group[neighbor] == group[current]:
                                return False
                        else:
                            group[neighbor] = -group[current]
                            queue.append(neighbor)
        return True
