class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited = set()
        a = headA
        b = headB

        while a:
            visited.add(a)
            a = a.next

       
        while b:
            if b in visited:
                return b
            b = b.next

        return None
