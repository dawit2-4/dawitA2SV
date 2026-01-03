class MinStack:

    def __init__(self):
        self.min = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            _, min_val = self.stack[-1]
            self.min = min(val, min_val)
        else:
            self.min = val
        self.stack.append((val, self.min))

    def pop(self) -> None:
        _, min_val = self.stack.pop()
        if self.stack:
            if min_val < self.stack[-1][0]:
                self.min = self.stack[-1][0]
        else:
            self.min = float('inf')
        

    def top(self) -> int:
        num, _ = self.stack[-1]
        return num
        

    def getMin(self) -> int:
        _, min_val = self.stack[-1]
        return min_val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()