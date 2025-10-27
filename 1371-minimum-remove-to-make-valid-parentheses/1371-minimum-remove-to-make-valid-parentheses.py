class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        count = 0
        res = []
        for c in s:
            if c == '(':
                res.append(c)
                count += 1
            elif c == ')':
                if count > 0:
                    res.append(c)
                    count -= 1
            else:
                res.append(c)
        
        ans = []
        for c in res[::-1]:
            if c == '(':
                if count == 0:
                    ans.append(c)
                else:
                    count -= 1
            else:
                ans.append(c)
        
        return "".join(ans[::-1])
            