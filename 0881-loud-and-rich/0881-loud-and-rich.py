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
                elif q > quiet[ans[child]]: 
                    q = quiet[ans[child]] 
                    n = ans[child] 

            ans[i] = n
            return(n , q)

        for i in range(len(quiet)):
            if i not in visited:
                visited.add(i)
                n, q = dfs(i)

                
        return ans
