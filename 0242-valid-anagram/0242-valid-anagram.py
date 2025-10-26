class Solution(object):
    def isAnagram(self, s, t):
        c1 = Counter(s)
        c2 = Counter(t)

        return c1 == c2

        