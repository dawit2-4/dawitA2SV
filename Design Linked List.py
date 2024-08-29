class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        current = self.head
        for _ in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        New_Node = ListNode(val, self.head)      
        self.head = New_Node
        self.size += 1
        


    def addAtTail(self, val: int) -> None:
        New_Node = ListNode(val)
        if not self.head:
            self.head = New_Node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = New_Node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return 
        elif index <= 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            New_Node = ListNode(val)
            current = self.head
            for _ in range(index-1):
                current = current.next
            New_Node.next = current.next
            current.next = New_Node

            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return 
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index-1):
                current = current.next
            current.next = current.next.next
        self.size -= 1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
