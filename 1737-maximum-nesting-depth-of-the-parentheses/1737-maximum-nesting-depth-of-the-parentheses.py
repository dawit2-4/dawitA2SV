class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        ans = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
                ans = max(ans, len(stack))
            elif s[i] == ')':
                stack.pop()
        return ans