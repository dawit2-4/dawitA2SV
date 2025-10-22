# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def dfs(node, summ):
            if not node.left and not node.right:
                return node.val + summ == targetSum
            left = dfs(node.left, summ +  node.val) if node.left else False
            right = dfs(node.right, summ + node.val) if node.right else False
            
            return left or right
        return dfs(root, 0)