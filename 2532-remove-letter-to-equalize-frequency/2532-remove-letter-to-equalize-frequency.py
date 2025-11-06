class Solution:
    def equalFrequency(self, word: str) -> bool:
        count = Counter(word)

        for key in list(count.keys()):
            count[key] -= 1
            if count[key] == 0:
                del count[key]
            if len(set(count.values())) == 1:
                return True
            count[key] += 1
        return False
        