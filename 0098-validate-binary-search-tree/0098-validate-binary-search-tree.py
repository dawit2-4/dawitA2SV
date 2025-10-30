# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = []
        def traverse(node):
            if not node:
                return 
            if node.left:
                traverse(node.left)
            ans.append(node.val)
            if node.right:
                traverse(node.right)
        traverse(root)
        if not ans:
            return True
        for i in range(1,len(ans)):
            if ans[i] <= ans[i-1]:
                return False
        return True
