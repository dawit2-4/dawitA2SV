class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        sett = set()
        longest = 0
        for r in range(len(s)):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1
            sett.add(s[r])
            window = (r -l) + 1
            longest = max(window, longest)
        return longest
