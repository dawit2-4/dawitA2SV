class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        n, m = len(word1), len(word2)
        merge = []
        while i < n and j < m:
            if word1[i:] >= word2[j:]:
                merge.append(word1[i])
                i += 1
            else:
                merge.append(word2[j])
                j += 1
        while i < n:
            merge.append(word1[i])
            i += 1
        while j < m:
            merge.append(word2[j])
            j += 1
        return ''.join(merge)
