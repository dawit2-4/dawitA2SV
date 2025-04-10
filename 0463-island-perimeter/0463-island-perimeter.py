class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
       
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))

        for  i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    perim = 4
                    for d in directions:
                        new_r = i + d[0]
                        new_c = j + d[1]
                        if inbound(new_r, new_c):
                            if grid[new_r][new_c] == 1:
                                perim -= 1
                else:
                    perim = 0
                perimeter += perim
        return perimeter