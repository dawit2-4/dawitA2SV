# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        store = {}
        def dp(root, rob):
            if not root:
                return 0
            if (root, rob) in store:
                return store[(root, rob)]
            

            
            changedRob = robbing = 0
            
            if rob:
                robbed = root.val + dp(root.right, not rob) + dp(root.left, not rob)            
                notRob = dp(root.left, rob) + dp(root.right, rob)
                
                robbing = max(robbed, notRob)
            else:
                changedRob = dp(root.left, not rob) + dp(root.right, not rob)
            store[(root, rob)] = max(robbing, changedRob)
            return store[(root,rob)]

        return dp(root, True)