# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans = ListNode()
        ptr = ans
        heap = []
        count = 0

        for node in lists:
            if node:
                heappush(heap, (node.val, count, node))
                count += 1
        while heap:
            val,_,smallest = heappop(heap)
            ptr.next = smallest
            ptr = ptr.next

            if smallest and smallest.next:
                heappush(heap, (smallest.next.val, count, smallest.next))
                count += 1
        return ans.next
            