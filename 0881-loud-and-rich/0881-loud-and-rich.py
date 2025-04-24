class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        for p1, p2 in richer:
            graph[p2].append(p1)
        x = max(quiet)
        ans = [0] * len(quiet)
        
        visited = set()
        
        # dfs
        def dfs(i):
            if not graph[i]:
                ans[i] = i
                return (i, quiet[i])
            q = quiet[i]
            n = i
            for child in graph[i]:
                if child not in visited:
                    visited.add(child)
                    n_new, q_new = dfs(child)
                    if q_new < q:
                        n = n_new
                        q = q_new
                elif q > quiet[ans[child]]: # instead of q > quiet[child]
                    # if the child is visited it means the child already have 
                    # the quietest one from the people who are richer than him 
                    # including it self

                    # so instead of comparing to the quiet of the child q should
                    # be compared with the quite of already quitest meaning, the one
                    # who is in the ans array  

                    q = quiet[ans[child]] # instead of q = quiet[child]
                    n = ans[child] # instead of n = child

            ans[i] = n
            return(n , q)

        for i in range(len(quiet)):
            if i not in visited:
                visited.add(i)
                n, q = dfs(i)

                
        return ans
