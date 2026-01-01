class Solution:
    def isValid(self, s: str) -> bool:
        closing = {"]":"[", "}":"{", ")":"("}
        stack = []

        for c in s:
            if c not in closing:
                stack.append(c)
            else:
                if stack:
                    opening = stack.pop()
                    if closing[c] != opening:
                        return False
                else:
                    return False
        return not stack
                    

        