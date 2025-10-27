class MagicDictionary:

    def __init__(self):
        self.dict = defaultdict(list)

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.dict[len(word)].append(word)

    def search(self, searchWord: str) -> bool:
        for word in self.dict[len(searchWord)]:
            change = 0
            for i in range(len(searchWord)):
                if word[i] != searchWord[i]:
                    if change > 1:
                        break
                    else:
                        change += 1
            if change == 1:
                return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)