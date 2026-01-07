"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        dummy = Node(0)
        stack = [head]
        ptr = dummy

        while stack:
            curr = stack.pop()
            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)
            ptr.next = curr
            curr.prev = ptr
            curr.child = None
            ptr = curr
        
        dummy.next.prev = None
        return dummy.next

        