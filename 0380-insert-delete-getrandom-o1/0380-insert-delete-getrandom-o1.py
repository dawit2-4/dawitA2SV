class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.mapped = {}
        
        
    def insert(self, val: int) -> bool:
        if val in self.mapped:
            return False
        else:
            self.mapped[val] = len(self.nums)
            self.nums.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.mapped:
            return False
        else:
            idx = self.mapped[val]
            last_num = self.nums[-1]
            self.nums[idx] = last_num
            self.mapped[last_num] = idx
            self.nums.pop()
            del self.mapped[val]
            return True

    def getRandom(self) -> int:
       return random.choice(self.nums)
        
        

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()