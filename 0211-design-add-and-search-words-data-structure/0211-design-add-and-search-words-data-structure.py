class WordDictionary:

    def __init__(self):
        self.children = [None] * 26
        self.is_end = False
    def char_to_index(self, char: str) -> int:
        return ord(char) -ord('a')

    def addWord(self, word: str) -> None:
        node = self
        for char in word:
            idx = self.char_to_index(char)
            if not node.children[idx]:
                node.children[idx] = WordDictionary()
            node = node.children[idx]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self
        stack = [(node, 0)]
        while stack:
            node, i = stack.pop()

            if i == len(word):
                if node.is_end:
                    return True
                continue
            
            w = word[i]
            if w == ".":
                for child in node.children:
                    if child:
                        stack.append((child, i+1))
            else:
                idx = self.char_to_index(w)
                if node.children[idx]:
                    stack.append((node.children[idx], i+1))
        return False




# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)