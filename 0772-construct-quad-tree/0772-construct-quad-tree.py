"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        l , r , t , b = 0, len(grid[0]) - 1, 0, len(grid) - 1
        def tree(l,r,t,b):
            sum_ = 0
            for i in range(t, b + 1):
                for j in range(l,r + 1):
                    sum_ += grid[i][j]
            if sum_ == 0 or sum_ == (r-l+1) ** 2:
                if sum_ == 0:
                    return Node(0,1,None, None, None, None)
                else:
                    return Node(1,1,None, None, None, None)
            
            mid_v = (t+b)//2
            mid_h = (l+r)//2

            top_left = tree(l, mid_h, t, mid_v)
            top_right = tree(mid_h+1, r, t, mid_v)
            bottom_left = tree(l, mid_h, mid_v+1, b)
            bottom_right = tree(mid_h+1, r, mid_v + 1, b)

            return Node(0,0,top_left,top_right,bottom_left, bottom_right)
        return tree(l,r,t,b)

