class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def inbound(row, col):
            return 0 <= row<len(maze) and 0 <=col<len(maze[0])
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        



        visited = set()
        visited.add((entrance[0], entrance[1]))
        queue = deque()

        queue.append(entrance)
        ans = 0
        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                
                for d in direction:
                    new_r = r + d[0]
                    new_c = c + d[1]

                    if inbound(new_r, new_c) :
                        if maze[new_r][new_c] == '.' and (new_r, new_c) not in visited:
                                queue.append((new_r, new_c))
                                visited.add((new_r,new_c))
                    elif [r,c] == entrance:
                        continue
                    else:
                        return ans
            ans += 1
        return -1
        


