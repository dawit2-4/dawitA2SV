class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        store = {"}":"{", ")":"(", "]":"["}

        for s in s:
            if s not in store:
                stack.append(s)
            else:
                if not stack:
                    return False
                else:
                    popped = stack.pop()
                    if popped != store[s]:
                        return False
        return not stack
