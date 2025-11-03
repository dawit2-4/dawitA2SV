# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        store = []
        curr = head
        while curr:
            store.append(curr.val)
            curr = curr.next
        print(store)
        i, j = 0, len(store) - 1
        curr = head
        while i <= j:
            if curr:
                curr.val = store[i]
                curr = curr.next
            i += 1
            
            if curr:
                curr.val = store[j]
                curr= curr.next
            j -= 1
        return head
