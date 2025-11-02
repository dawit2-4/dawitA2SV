# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        s = defaultdict(list)

        def dfs(node, row, col):
            nonlocal s
            s[col].append((row, node.val))
            

            if node.left:
                dfs(node.left, row + 1,col - 1)
            if node.right:
                dfs(node.right,row + 1, col + 1)
            return
        dfs(root,0,0)
        ans = []
        for col in sorted(s.keys()):
            row_vals = [val for row,val in sorted(s[col])]
            ans.append(row_vals)
        return ans