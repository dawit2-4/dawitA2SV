class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        queue = deque()
        visited = set()
        for r in range(len(isWater)):
            for c in range(len(isWater[0])):
                if isWater[r][c] == 1:
                    queue.append([r,c])
                    visited.add((r,c))
                    isWater[r][c] = 0
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        def inbound(row, col):
            return 0 <= row<len(isWater) and 0 <=col<len(isWater[0])
        
        
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                for d in direction:
                    new_r = r + d[0]
                    new_c = c + d[1]

                    if inbound(new_r, new_c) and (new_r, new_c) not in visited:
                        isWater[new_r][new_c] = isWater[r][c] + 1
                        queue.append([new_r, new_c])
                        visited.add((new_r, new_c))
        return isWater
                