from collections import defaultdict
from typing import List

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        ancestors = defaultdict(set)
        visited = [False] * n
        
        # Reverse graph: child -> list of parents
        for parent, child in edges:
            graph[child].append(parent)

        def dfs(node):
            if visited[node]:
                return ancestors[node]
            visited[node] = True
            for parent in graph[node]:
                ancestors[node].add(parent)
                ancestors[node].update(dfs(parent))
            return ancestors[node]

        result = []
        for i in range(n):
            dfs(i)
            result.append(sorted(ancestors[i]))  # Sorted list as required
        return result
