class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def inbound(r, c):
            return 0 <= r < len(image) and 0 <= c < len(image[0])
        direction = ((0,1),(0,-1),(1,0),(-1,0))

        queue = deque()
        queue.append([sr,sc])
        z = image[sr][sc]
        image[sr][sc] = color
        visited = set()
        while queue:
            # for _ in range(len(queue)):
            r, c = queue.popleft()
            for dr , dc in direction:
                new_r = r + dr
                new_c = c + dc

                if inbound(new_r,new_c) and image[new_r][new_c] == z  and (new_r, new_c) not in visited:
                    visited.add((new_r, new_c))
                    queue.append([new_r, new_c])
                    image[new_r][new_c] = color
        
        return image
