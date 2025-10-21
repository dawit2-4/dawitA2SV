class Trie():
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False
        self.count = 0
    
class Solution:
    def __init__(self):
        self.root = Trie()
    def char_to_idx(self, char):
        return ord(char) - ord('a')
    def search(self, word):
        node  = self.root
        for c in word:
            idx = self.char_to_idx(c)
            if not node.children[idx]:
                return False
            node = node.children[idx]
            if not node.is_end:
                return False
        return True
    def longestWord(self, words: List[str]) -> str:
        root = self.root
        for word in words:
            node = root
            for char in word:
                idx = self.char_to_idx(char)
                if not node.children[idx]:
                    node.children[idx] = Trie()
                node = node.children[idx]
                node.count += 1
            node.is_end = True
        max_count = 0
        ans = ""
        words.sort()
        for word in words:
            if self.search(word):
                if len(word) > max_count:
                    max_count = len(word)
                    ans = word
        return ans
        


