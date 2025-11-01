class Solution:
    def longestBalanced(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            store = Counter()
            for j in range(i,len(s)):
                store[s[j]] += 1
                if len(set(store.values())) == 1:
                    ans = max(ans, j - i + 1)
        return ans