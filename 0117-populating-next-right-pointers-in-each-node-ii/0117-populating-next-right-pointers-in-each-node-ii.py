"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # deque (node) on the same level
        queue = deque()

        if not root:
            return root
        
        queue.append(root)

        # traverse over the tree
        while queue:

            n = len(queue) #traverse level order
            prev = None 

            for _ in range(n):
                node = queue.popleft()
                if prev:
                    prev.next = node
                prev = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root