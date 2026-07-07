class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = defaultdict(int)
        left = 0
        longest = 0
        for right in range(len(s)):
            count[s[right]] += 1
            while count[s[right]] > 1 and left <= right:
                count[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest

        