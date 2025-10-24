class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        ans = ''
        i = len(s) - 1

        while i >= 0:
            if s[i] != '[':
                stack.append(s[i])
                i -= 1
            else:
                sub = ''
                while stack and stack[-1] != ']':
                    sub += stack.pop()
                
                stack.pop()
                num = ''
                i -= 1
                while i >= 0 and s[i].isdigit():
                    num = s[i] + num
                    i -= 1
                sub = sub * int(num)
                stack.append(sub)

        return ''.join(stack[::-1])