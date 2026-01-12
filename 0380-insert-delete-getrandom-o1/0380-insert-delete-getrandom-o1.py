class RandomizedSet:

    def __init__(self):
        self.random_set = {}
        self.random_array = []

    def insert(self, val: int) -> bool:
        if val not in self.random_set:
            n = len(self.random_array)
            self.random_set[val] = n
            self.random_array.append(val)
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        if val in self.random_set:
            idx = self.random_set[val]

            last_val = self.random_array[-1]
            self.random_array[idx] = last_val
            self.random_set[last_val] = idx
            del self.random_set[val]
            self.random_array.pop()

            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.random_array)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()