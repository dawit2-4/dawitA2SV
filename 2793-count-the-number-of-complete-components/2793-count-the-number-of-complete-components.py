class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for node, neighbour in edges:
            graph[node].append(neighbour)
            graph[neighbour].append(node)
        visited = set()
        count = 0
        queue = deque()

        def dfs(i):
            nodes = []
            queue.append(i)
            
            while queue:
                num = queue.popleft()
                nodes.append(num)
                for child in graph[num]:
                    if child not in visited:
                        queue.append(child)
                        visited.add(child)
            for node in nodes:
                if len(graph[node]) != len(nodes) - 1:
                    return False
            return True
        for i in range(n):
            if i not in visited:
                visited.add(i)
                if dfs(i):
                    count += 1
        return count
                        


        
        