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
        def dfs(node, i):
            if i == len(word):
                return node.is_end
            if word[i] == ".":
                for child in node.children:
                    if child and dfs(child, i+1):
                        return True
                return False
            else:
                idx = self.char_to_index(word[i])
                if not node.children[idx]:
                    return False
                return dfs(node.children[idx], i+1)
        return dfs(self, 0)




# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)