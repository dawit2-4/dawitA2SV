class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == "+":
                x, y = stack.pop(),stack.pop()
                stack.append(x+y)
            elif tokens[i] == "*":
                x, y = stack.pop(),stack.pop()
                stack.append(x*y)
            elif tokens[i] == "-":
                x, y = stack.pop(),stack.pop()
                stack.append(y-x)
            elif tokens[i] == "/":
                x, y = stack.pop(),stack.pop()
                ans = y/x
                if ans < 0:
                    stack.append(ceil(y/x))
                else:
                    stack.append(y//x)
            else:
                stack.append(int(tokens[i]))
        return stack[-1]