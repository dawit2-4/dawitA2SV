# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = l1
        node2 = l2
        ans = ListNode()
        ptr = ans
        carry = 0
        while node1 or node2 or carry:
            v1 = node1.val if node1 else 0
            v2 = node2.val if node2 else 0
            summ = v1 + v2 + carry
            carry = summ // 10
            val = summ % 10
            
            ptr.next = ListNode(val)
            ptr = ptr.next

            if node1:
                node1 = node1.next
            if node2: 
                node2 = node2.next
        return ans.next

        
        carry = 0
        