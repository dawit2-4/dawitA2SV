# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        ptr =dummy
        if not head:
            return head
        
        node = head
        while node:
            if node.val != val:
                new = ListNode(node.val)
                ptr.next = new
                ptr = ptr.next
            node = node.next
        return dummy.next
