class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for idx, (nom, den) in enumerate(equations):
            graph[nom].append((den, values[idx]))
            graph[den].append((nom, 1/values[idx]))
        
        def dfs(nom, den, visited):
            if nom == den:
                return 1.0
                
            visited.add(nom)
            for neigh, weight in graph[nom]:
                if neigh not in visited:
                    res = dfs(neigh, den, visited)
                    if res != -1.0:
                        return res * weight

            return -1.0
        
        ans = []
        for a, b in queries:
            if a not in graph or b not in graph:
                ans.append(-1.0)
            else:
                ans.append(dfs(a, b, set()))
        
        return ans