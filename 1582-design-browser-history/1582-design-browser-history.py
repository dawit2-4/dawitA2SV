class LinkedList():
    def __init__(self, val="", next=None, prev=None):
        self.val = val
        self.next = next
        self.prev =  prev
class BrowserHistory:

    def __init__(self, homepage: str):
        root = LinkedList(homepage, None, None)
        self.curr = root

    def visit(self, url: str) -> None:
        New_Node = LinkedList(url)
        self.curr.next = New_Node
        New_Node.prev = self.curr
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        while self.curr.prev and steps > 0:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.val

    def forward(self, steps: int) -> str:
        while self.curr.next and steps > 0:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)