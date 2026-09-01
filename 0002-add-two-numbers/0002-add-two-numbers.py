# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0)
        ptr = ans
        carry = 0

        while l1 and l2:
            summ = l1.val + l2.val + carry
            if summ >= 10:
                reminder = summ % 10
                ptr.next = ListNode(reminder)
                carry = 1
            else:
                carry = 0
                ptr.next = ListNode(summ) 
            
            ptr = ptr.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            summ = l1.val + carry
            if summ >= 10:
                reminder = summ % 10
                ptr.next = ListNode(reminder)
                carry = 1
            else:
                carry = 0
                ptr.next = ListNode(summ)
            l1 = l1.next
            ptr = ptr.next
        while l2:
            summ = l2.val + carry
            if summ >= 10:
                reminder = summ % 10
                ptr.next = ListNode(reminder)
                carry = 1
            else:
                carry = 0
                ptr.next = ListNode(summ)
            l2 = l2.next
            ptr = ptr.next
        if carry == 1:
            ptr.next = ListNode(1)
        return ans.next

