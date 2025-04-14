# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append((root, 0))
        ans = []
        result = []

        while queue:
            node, level = queue.popleft()
            
            if node:
                ans.append((node.val,level))
                if node.left:
                    queue.append((node.left, level+1))
                if node.right:
                    queue.append((node.right, level+1))
        res = [[] for _ in range(len(ans))]
        for val, level in ans:
            res[level].append(val)
        for comb in res:
            if len(comb) > 0:
                result.append(comb)
        return result