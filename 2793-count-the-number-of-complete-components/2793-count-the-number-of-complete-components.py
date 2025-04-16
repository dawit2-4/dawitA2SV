class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for node, neighbour in edges:
            graph[node].append(neighbour)
            graph[neighbour].append(node)
        visited = set()
        count = 0

        def dfs(i):
            arr = [i]
            for child in graph[i]:
                if child not in visited:
                    visited.add(child)
                    new_a = dfs(child)
                    arr.extend(new_a)
            
            return arr

            
        for i in range(n):
            if i not in visited:
                visited.add(i)
                nodes = dfs(i)
                complete = True
                for node in nodes:
                    if len(graph[node]) != len(nodes) - 1:
                        complete = False
                        break
                if complete:
                    count += 1

                
        return count
                        


        
        