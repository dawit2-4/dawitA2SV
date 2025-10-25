class OrderedStream:

    def __init__(self, n: int):
        self.arr = [0] * (n + 1)
        self.index = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.arr[idKey] = value
        ans = []
        while self.index < len(self.arr) and self.arr[self.index] != 0:
            ans.append(self.arr[self.index])
            self.index += 1
        return ans


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)