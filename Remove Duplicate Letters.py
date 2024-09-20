class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lookUp = {}
        seen = set()
        stack = []

        for i in range(len(s)):
            lookUp[s[i]] = i
        
        for i in range(len(s)):
            if s[i] in seen: continue
            while stack and stack[-1] > s[i] and lookUp[stack[-1]] > i:
                seen.remove(stack[-1])
                stack.pop()
            stack.append(s[i])
            seen.add(s[i])

        return "".join(stack)
