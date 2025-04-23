class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        
        for course, pre in prerequisites:
            graph[pre].append(course)
            in_degree[course] += 1
        
        ans = []
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        while queue:
            for _ in range(len(queue)):
                num = queue.popleft()
                ans.append(num)

                for child in graph[num]:
                    in_degree[child] -= 1
                    if in_degree[child] == 0:
                        queue.append(child)
        if len(ans) == numCourses:
            return ans
        else:
            return []
