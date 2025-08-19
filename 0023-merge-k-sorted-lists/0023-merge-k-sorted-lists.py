# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for node in lists:
            l = node 
            while l:
                arr.append(l.val)
                l = l.next
        ans = ListNode(0)
        l = ans
        arr.sort()
        for num in arr:
            l.next = ListNode(num)
            l = l.next
        return ans.next
        
        