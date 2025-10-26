class MagicDictionary:

    def __init__(self):
        self.dict = []

    def buildDict(self, dictionary: List[str]) -> None:
        self.dict += dictionary

    def search(self, searchWord: str) -> bool:
        ans = False
        for word in self.dict:
            if len(word) !=len(searchWord):
                ans |= False
                continue
            i = count = 0
            while i < len(searchWord):
                if word[i] != searchWord[i]:
                    if count == 0:
                        count += 1
                        i += 1
                        continue
                    else:
                        ans |= False
                        break
                i += 1
            if count == 1 and i == len(word):
                ans |= True
            else:
                ans |= False
        return ans
            
            


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)