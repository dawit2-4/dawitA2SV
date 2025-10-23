class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_set = defaultdict(int)
        l = 0 
        r = 0
        max_count = 0
        while r <len(s):
            hash_set[s[r]] += 1
            while hash_set[s[r]] > 1 and l <= r:
                hash_set[s[l]] -= 1
                l += 1
            max_count =max(max_count, r-l+1)
            r += 1
        return max_count