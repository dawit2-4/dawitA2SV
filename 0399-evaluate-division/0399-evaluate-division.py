class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i, (start, end) in enumerate(equations):
            graph[start].append((end, values[i]))
            graph[end].append((start, 1 / values[i]))
        
        def dfs(node, visited, end):
            if node == end:
                return 1.00
            visited.add(node)

            for neighbour, value in graph[node]:
                if neighbour not in visited:
                    result = dfs(neighbour, visited, end)
                    if result != -1.00:
                        return result * value
            
            return -1.00
        answer = []
        for start, end in queries:
            if start not in graph:
                answer.append(-1.00)
                continue
            result = dfs(start, set(), end)
            answer.append(result)
        return answer