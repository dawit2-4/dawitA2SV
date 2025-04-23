class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        visited = set()
        for course, pre in prerequisites:
            graph[course].append(pre)
        print(graph)
        stack = []
        
        def dfs(num, path):
            if len(graph[num]) == 0:
                visited.add(num)
                stack.append(num)
                path.add(num)
                return True
            
            if num in path:
                return False
            path.add(num)
            for child in graph[num]:
                if child not in visited:
                    if not dfs(child, path):
                        return False
            visited.add(num)
            stack.append(num)
            return True
            
                    
        
        for i in range(numCourses):
            if i not in visited:
                if not dfs(i,set()):
                    return []
        # ans = []
        # while stack:
        #     ans.append(stack.pop())
        return stack
            

