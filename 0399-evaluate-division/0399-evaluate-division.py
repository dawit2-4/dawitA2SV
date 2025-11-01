class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list) #(start -> (end, 3.00) and end -> (start, 1/3.00))
        for i, node in enumerate(equations):
            graph[node[0]].append((node[1], values[i]))
            graph[node[1]].append((node[0], 1/values[i]))
        
        # flag = True
        def dfs(node, target,  visited):
            if node == target:
                return 1.000
            for child in graph[node]:
                (next, val) = child
                if (next, val) not in visited:
                    visited.add((next, val))
                    res = dfs(next, target, visited)

                    if res != -1:
                        return val * res

            return -1.00
        ans = []
        for s, e in queries:
            if s not in graph or e not in graph:
                ans.append(-1.0000)
            else:
                ans.append(dfs(s, e, set()))
        return ans
                 