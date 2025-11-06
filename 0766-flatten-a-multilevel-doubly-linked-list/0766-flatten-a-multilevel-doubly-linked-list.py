# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        stack = [head] # node
        dummy = Node(0, None, None, None)
        current = dummy

        # iterate over our linked list until the stack is empty
        while stack:
            node = stack.pop()

            current.next = node
            node.prev = current
            if node.next:
                stack.append(node.next)
            if node.child:
                stack.append(node.child)

            node.child = None
            current = current.next
        dummy.next.prev = None
        return dummy.next
        