class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        def inbound(row, col):
            return 0 <= row<len(grid) and 0 <=col<len(grid[0])
        queue = deque()
        fresh = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append([r,c])
                elif grid[r][c] == 1:
                    fresh += 1
            
        if fresh == 0:
            return 0
        time = 0

        while queue:
            c = len(queue)
            for _ in range(c):
                r, c = queue.popleft()
                for d in direction:
                    new_r = r + d[0]
                    new_c = c + d[1]

                    if inbound(new_r, new_c) and grid[new_r][new_c] == 1:
                        fresh -= 1
                        grid[new_r][new_c] = 2
                        queue.append([new_r,new_c])
            time += 1
        if fresh == 0:
            return time - 1
        else:
            return -1


                
                