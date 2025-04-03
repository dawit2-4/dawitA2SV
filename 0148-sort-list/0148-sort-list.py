# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(left_half, right_half):
         
            merge = n_head = ListNode()
            left = left_half
            right = right_half

            while left and right:
                if left.val < right.val:
                    merge.next = left
                    left = left.next
                else:
                    merge.next = right
                    right = right.next
                merge = merge.next
            if left:
                merge.next = left
             
               
            if right:
                merge.next = right
               
            return n_head.next
        l = ListNode()
        def mergeSort(head):
            if not head or not head.next:
                return head
            slow = head
            fast = head.next

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            right = slow.next
            slow.next = None
            l = mergeSort(head)
            r = mergeSort(right)
            

            return merge(l,r)
       
        return mergeSort(head)