# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        
        oddpointer = current = head
        evenpointer = evenhead = head.next
        i = 1

        while current:
            if i > 2 and i % 2 != 0:
                oddpointer.next = current
                oddpointer = oddpointer.next
            elif i > 2 and i % 2 == 0:
                evenpointer.next = current
                evenpointer = evenpointer.next
            current = current.next
            i += 1
        
        evenpointer.next = None
        oddpointer.next = evenhead

        return head
