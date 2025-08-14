class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i, node in enumerate(equations):
            x, y = node
            graph[x].append((y,values[i]))
            graph[y].append((x,1/values[i]))
       
        def dfs(node,end, val, visited):
            if node == end:
                return val
            visited.add(node)
            for child, value in graph[node]:
                if child not in visited:
                    result = dfs(child, end, (val * value), visited)
                    if result != -1:
                        return result
            return -1
        ans = []      
        for start, end in queries:
            if start not in graph or end not in graph:
                ans.append(-1.00000)
            else:
                result = dfs(start, end, 1, set()) 
                ans.append(result)
        return ans
            