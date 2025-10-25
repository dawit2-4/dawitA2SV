"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
from typing import Optional


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        dummy = Node(None, None, head, None)

        def dfs(prev, curr):
            if not curr:
                return prev
            
            curr.prev = prev
            prev.next = curr

            tnext = curr.next
            tail = dfs(curr, curr.child)
            curr.child = None
            return dfs(tail, tnext)
        dfs(dummy, head)
        dummy.next.prev = None
        return dummy.next
            
