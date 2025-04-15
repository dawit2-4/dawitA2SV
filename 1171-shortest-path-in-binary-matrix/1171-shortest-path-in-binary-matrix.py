class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        visited.add((0,0))
        queue = deque()
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1
        queue.append([0,0])
        direction = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
        def inbound(row, col):
            return 0 <= row<len(grid) and 0 <=col<len(grid[0])

        ans = 1
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r == n-1 and c == n -1:
                    return ans 
                
                for d in direction:
                    new_r = r + d[0]
                    new_c = c + d[1]
                    
                    if (new_r, new_c) not in visited and inbound(new_r, new_c) and grid[new_r][new_c] == 0:
                        visited.add((new_r, new_c))
                        queue.append([new_r,new_c])
                        
                
            ans += 1
        return -1
