class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        occur = {0:-1}
        ans = 0
        state = 0
        vowel = {'a':1, 'e':2, 'i':4, 'o':8, 'u':16}
        for i in range(len(s)):
            if s[i] in vowel:
                state ^= vowel[s[i]]
            if state in occur:
                ans = max(ans, i-occur[state])
            else:
                occur[state] = i
        return ans
