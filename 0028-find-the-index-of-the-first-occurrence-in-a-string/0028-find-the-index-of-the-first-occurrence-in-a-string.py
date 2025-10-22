class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        j = len(needle) - 1
        while j < len(haystack):
            bola = True
            for k in range(len(needle)):
                if haystack[i+k] != needle[k]:
                    bola = False
            if bola:
                return i
            i += 1
            j += 1
        return -1
