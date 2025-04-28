class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for c1, c2 in prerequisites:
            graph[c1].append(c2)
        ans = [] 
        def dfs(node, parent, visited):
            if node == parent:
                return True
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    if dfs(neighbour, parent, visited):
                        return True
            return False
        for parent , ch in queries:
            ans.append(dfs(parent,ch, set()))
        return ans
