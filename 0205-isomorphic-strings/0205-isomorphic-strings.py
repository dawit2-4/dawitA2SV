class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        store = {}
        store2 = {}
        for i in range(len(s)):
            if s[i] in store:
                if store[s[i]] != t[i]:
                    return False
            else:
                store[s[i]] = t[i]
            if t[i] in store2:
                if store2[t[i]] != s[i]:
                    return False
            else:
                store2[t[i]] = s[i]
        return True