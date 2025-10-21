class Trie():
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False
        self.count = 0

class MapSum:

    def __init__(self):
        self.root = Trie()
        self.was_before = {}
    
    def char_to_idx(self, char):
        return ord(char) - ord('a')

    def insert(self, key: str, val: int) -> None:
        node = self.root
        if key not in self.was_before:
            for ch in key:
                idx =  self.char_to_idx(ch)
                if not node.children[idx]:
                    node.children[idx] = Trie()
                node = node.children[idx]
                node.count += val
            node.is_end = True
        else:
            for ch in key:
                idx =  self.char_to_idx(ch)
                node = node.children[idx]
                node.count = node.count - self.was_before[key] + val
        self.was_before[key] = val
             
    def sum(self, prefix: str) -> int:
        node = self.root
        count = 0
        for ch in prefix:
            idx = self.char_to_idx(ch)
            if node.children[idx]:
                count = node.children[idx].count
                node = node.children[idx]
               
            else:
                return 0
            
        return count
   


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)