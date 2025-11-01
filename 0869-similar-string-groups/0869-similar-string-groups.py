class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        def is_similar(a, b):
            count = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    count += 1
            return count == 0 or count == 2
        visited = set()
        def dfs(i):
            for j in range(n):
                if j not in visited and is_similar(strs[i], strs[j]):
                    visited.add(j)
                    dfs(j)
        component = 0
        for i in range(n):
            if i not in visited:
                component += 1
                visited.add(i)
                dfs(i)
        return component