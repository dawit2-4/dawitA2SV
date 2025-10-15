class Trie:

    def __init__(self):
        self.children = [None] * 26
        self.is_end = False
    
    def char_to_index(self, char: str) -> int:
        return ord(char) - ord('a')

    def insert(self, word: str) -> None:
        node = self
        for char in word:
            idx = self.char_to_index(char)
            if not node.children[idx]:
                node.children[idx] = Trie()
            node = node.children[idx]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self
        for char in word:
            idx = self.char_to_index(char)
            if not node.children[idx]:
                return False
            node = node.children[idx]
        return node.is_end


    def startsWith(self, prefix: str) -> bool:
        node = self
        for char in prefix:
            idx = self.char_to_index(char)
            if not node.children[idx]:
                return False
            node = node.children[idx]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)