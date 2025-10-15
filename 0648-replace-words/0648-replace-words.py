class Trie():
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False
class Solution:
    def __init__(self):
        self.root = Trie()
    def char_to_index(self, char: str) -> int:
        return ord(char) - ord('a')

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = self.root
        for word in dictionary:
            node = root
            for c in word:
                idx = self.char_to_index(c)
                if  not node.children[idx]:
                    node.children[idx] = Trie()
                node = node.children[idx]
            node.is_end = True
        ans = []

        sentence = sentence.split()
        for word in sentence:
            root_word = []
            node = root
            for c in word:
                idx = self.char_to_index(c)
                if not node.children[idx] or node.is_end:
                    break
                else:
                    root_word.append(c)
                    node = node.children[idx]
            if node.is_end:
                ans.append("".join(root_word))
            else:
                ans.append(word)
        res = ""
        for word in ans:
            res += word
            res += " "
        return res.rstrip()
        