class Trie():
    def __init__(self):
        self.children = [None] * 26
        self.count = 0
        self.is_end = False
    
    
class Solution:
    def __init__(self):
        self.root = Trie()
    def char_to_index(slef, char):
        return ord(char) - ord('a')
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = self.root
        for word in words:
            node = root
            for w in word:
                idx = self.char_to_index(w)
                if not node.children[idx]:
                    node.children[idx] = Trie()
                node.children[idx].count += 1
                node = node.children[idx]
            node.is_end = True
        ans = []
        for word in words:
            node = root
            count = 0
            for w in word:
                idx = self.char_to_index(w)
                if node.children[idx]:
                    node = node.children[idx]
                    count += node.count
            ans.append(count)
        # print(root.children)
        return ans