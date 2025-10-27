class MagicDictionary:

    def __init__(self):
        self.patterns = defaultdict(set)

    def buildDict(self, dictionary: List[str]) -> None:
        for word  in dictionary:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                self.patterns[pattern].add(word)

    def search(self, searchWord: str) -> bool:
        for i in range(len(searchWord)):
            pattern = searchWord[:i] + "*" + searchWord[i+1:]
            if pattern in self.patterns:
                for child in self.patterns[pattern]:
                    if child != searchWord:
                        return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)