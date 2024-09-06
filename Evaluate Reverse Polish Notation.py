class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for s in tokens:
            if s == "+" or s == "*" or s == "/" or s == "-":
                b, a = stack.pop(), stack.pop()
                if s == "+":
                    stack.append(a+b)
                elif s == "-":
                    stack.append(a-b)
                elif s == "/":
                    div = a / b
                    if div < 0:
                        stack.append(ceil(div))
                    else:
                        stack.append(floor(div))
                elif s == "*" :
                    stack.append(a*b)
            else:
                stack.append(int(s))
        return stack.pop()
