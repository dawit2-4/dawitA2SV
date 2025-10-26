class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')


    def push(self, val: int) -> None:
        self.min = min(self.min, val)
        self.stack.append((val, self.min))

    def pop(self) -> None:
        val, _ = self.stack.pop()
        if self.stack:
            _, m = self.stack[-1]
            self.min = m
        else:
            self.min = float('inf')
        return val

    def top(self) -> int:
        val, _ = self.stack[-1]
        return val

    def getMin(self) -> int:
        _, min_val = self.stack[-1]
        return min_val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()