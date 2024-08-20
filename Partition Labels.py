class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx = {}
        start, end = 0, 0
        ans = []
        # for i in range(len(s)):
        #     if s[i] not in last_idx:
        #         last_idx[s[i]] = i
        #     elif last_idx[s[i]] < i:
        #         last_idx[s[i]] = i
        last_idx = {char: idx for idx, char in enumerate(s)}
        for i in range(len(s)):
            end = max(end, last_idx[s[i]])
            if end == i:
                ans.append(end - start + 1)
                start = i + 1
        return ans
