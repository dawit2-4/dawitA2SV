# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append(root)
        num = root.val
        while queue:
            new_num = queue.popleft()
            if new_num:
                if new_num.val != num:
                    return False
                queue.append(new_num.left)
                queue.append(new_num.right)
        return True