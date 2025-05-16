class Solution:
    def longestAwesome(self, s: str) -> int:
        bits = {}
        for i in range(10):
            bits[i] = 2 ** i
        occur = {0:-1}
        l = 0
        state = 0
        ans = 0
        for i in range(len(s)):
            state ^= bits[int(s[i])]
            if state.bit_count() >= 1:
                for j in range(10):
                    x = 1 << j
                    if x ^ state in occur:
                        ans = max(ans, i - occur[x^state])
           
            if state in occur:
                if state == 0:
                    ans = max(ans, i+1)
                else:
                    ans = max(ans, i - occur[state] + 1)
            else:
                occur[state] = i
        return ans
