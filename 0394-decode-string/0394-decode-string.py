class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):

            if s[i] != ']':
                stack.append(s[i])
            else:
                string = []
                number = []
                
                while stack[-1] != '[':
                    string.append(stack.pop())
                stack.pop()
    
                while stack and stack[-1].isdigit():
                    number.append(stack.pop())

                reversed_string = "".join(reversed(string))
                reversed_number = "".join(reversed(number))
                stack.append(int(reversed_number) * reversed_string)
                
        return "".join(stack)
        