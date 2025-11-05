class Solution:
    def allPathsSourceTarget(self, graphs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list) # node -> [child1, child2 ....]
        
        for i in range(len(graphs)):
            graph[i] = graphs[i]
        
        paths = []
        def dfs(node, path):
            if node == len(graphs) - 1:
                paths.append(path[:])
                return
            
            for child in graph[node]:
                path.append(child)
                dfs(child, path)
                path.pop()
            
        dfs(0, [0])
        return paths