class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        my_list = defaultdict(list)
        for i in range(len(graph)):
            my_list[i] = graph[i]
        ans = []
        def dfs(node, arr):
            if node == len(graph) - 1:
                arr.append(node)
                ans.append(arr[:])
                return 
            for child in my_list[node]:
                dfs(child, arr + [node])
            return
        dfs(0, [])
        return ans
        