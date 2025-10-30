# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque()
        q.append(root)
        ans = []

        while q:
            n = len(q)
            for i in range(n):
                if i == n - 1:
                    x = q.popleft()
                    ans.append(x.val)
                else:
                    x = q.popleft()
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
        return ans