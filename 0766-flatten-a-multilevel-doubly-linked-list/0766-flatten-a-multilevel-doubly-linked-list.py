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

        def dfs(curr, prev):
            if not curr:
                return prev
            
            prev.next = curr
            curr.prev = prev

            temp_next = curr.next
            tail = dfs(curr.child, curr)
            curr.child =None
            return dfs(temp_next, tail)
        dfs(head, dummy)
        dummy.next.prev = None
        return dummy.next
            
