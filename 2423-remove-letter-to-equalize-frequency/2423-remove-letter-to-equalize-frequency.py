class Solution:
    def equalFrequency(self, word: str) -> bool:
        count = Counter(word)        
        for c in word:
            count[c] -= 1
            if count[c] == 0:
                del count[c]
            # print(c, count[c], list(count.values()))
            if len(set(count.values())) == 1:
                return True
            count[c] += 1
            # print(c, count[c])
        return False
            
            



