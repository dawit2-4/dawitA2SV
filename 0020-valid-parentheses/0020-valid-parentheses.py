class Solution:
    def isValid(self, s: str) -> bool:
        hash_set = { ")" : "(", "]" : "[", "}" : "{"}
        stack = []

        for i in range(len(s)):
            if s[i] in hash_set:
                if stack and stack[-1] == hash_set[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        return not stack