class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [(s[0], 1)]

        for i in range(1,len(s)):
            if stack:
                st, ct = stack[-1]
                
                if s[i] == st:
                    if (ct + 1) == k:
                        stack.pop()
                    else:
                        stack.pop()
                        stack.append((st, ct + 1))
                else:
                    stack.append((s[i], 1))
            else:
                stack.append((s[i], 1))
        ans = ''
        for st, ct in stack:
            new = st * ct
            ans += new
        return ans
        
            