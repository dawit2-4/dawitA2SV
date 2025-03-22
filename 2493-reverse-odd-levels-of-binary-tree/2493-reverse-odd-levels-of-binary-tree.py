# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])
        i = 0

        while queue:
            if i % 2 == 1:
                l = 0
                r = len(queue) - 1

                while l < r:
                    queue[l].val, queue[r].val = queue[r].val, queue[l].val
                    l += 1
                    r -= 1

            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            i += 1
        return root