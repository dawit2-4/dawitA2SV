class Solution:
    def equalFrequency(self, word: str) -> bool:
        count = Counter(word)
        for ch in list(count.keys()):
            count[ch] -= 1
            if count[ch] == 0:
                del count[ch]
            s = set(count.values())
            if len(s) == 1:
                return True
            count[ch] += 1
        return False
            
            