class Solution:
    def firstUniqChar(self, s: str) -> int:
        store = defaultdict(int)
        for i in range(len(s)):
            store[s[i]] += 1

        for i in range(len(s)):

            if store[s[i]] == 1:
                return i
            
        return -1