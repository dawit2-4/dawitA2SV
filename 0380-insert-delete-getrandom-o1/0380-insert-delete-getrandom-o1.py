class RandomizedSet:

    def __init__(self):
        self.RandomizedSet = []
        self.indices = {}

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        self.RandomizedSet.append(val)
        self.indices[val] = len(self.RandomizedSet) -1
        return True


    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        self.indices[self.RandomizedSet[-1]] = self.indices[val]
        
        self.RandomizedSet[self.indices[val]], self.RandomizedSet[-1] = self.RandomizedSet[-1], self.RandomizedSet[self.indices[val]]

        del self.indices[val]
        self.RandomizedSet.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.RandomizedSet)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()