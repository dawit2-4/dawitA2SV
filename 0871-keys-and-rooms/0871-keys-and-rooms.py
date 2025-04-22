class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        set_ = set()
        graph = defaultdict(list)

        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                graph[i].append(rooms[i][j])
                    
        
        queue = deque()
        queue.append(0)
        visited = set()
        print(graph, queue)
        def dfs():
            while queue:
                num = queue.popleft()
                if num not in visited:
                    visited.add(num)
                    for child in graph[num]:
                        queue.append(child)
        dfs()
        
        for i in range(1,len(rooms)):
            if i not in visited:
                return False
        print(graph, visited)
        return True