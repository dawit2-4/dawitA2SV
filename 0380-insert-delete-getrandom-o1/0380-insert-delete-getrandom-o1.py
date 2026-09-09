class RandomizedSet:

    def __init__(self):
        self.number_set = {}
        self.number_array = []

    def insert(self, val: int) -> bool:
        if val not in self.number_set:
            self.number_set[val] = len(self.number_array)
            self.number_array.append(val)
            return True
            
        else:
            return False


    def remove(self, val: int) -> bool:
        if val in self.number_set:
            self.number_set[self.number_array[-1]] = self.number_set[val]
            self.number_array[self.number_set[val]], self.number_array[-1] = self.number_array[-1], self.number_array[self.number_set[val]]
            self.number_array.pop()
            del self.number_set[val]
            
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.number_array)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()