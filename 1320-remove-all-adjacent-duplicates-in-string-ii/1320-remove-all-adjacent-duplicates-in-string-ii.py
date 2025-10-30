class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [(s[0], 1)]
        i = 1
        while i < len(s):
            if stack:
                if s[i] ==stack[-1][0]:
                    st, count = stack.pop()
                    if count + 1 != k:
                        stack.append((s[i],count+1))
                else:
                    stack.append((s[i],  1))
            else:
                stack.append((s[i],  1))
            i += 1
        ans = ""
        for s, c in stack:
            ans = ans + ((s)*c)
        return ans