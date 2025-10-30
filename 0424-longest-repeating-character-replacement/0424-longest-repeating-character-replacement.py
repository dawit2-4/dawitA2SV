class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_store = defaultdict(int)
        j = 0
        max_substring = 0
        most_freq = 0
        for i in range(len(s)):
            char_store[s[i]] += 1
            most_freq = max(most_freq, char_store[s[i]])
            while (i-j+1) - most_freq > k:
                char_store[s[j]] -= 1
                j += 1
            max_substring = max((i-j+1), max_substring)
        return max_substring

