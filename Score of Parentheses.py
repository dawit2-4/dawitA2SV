class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0
        
        for char in s:
            if char == '(':
                stack.append(score)
                score = 0
            else:
                score = stack.pop() + max(2 * score, 1)
        
        return score

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        bal = 0
        ans = 0
        for i in range(len(s)):
            if s[i] == "(":
                bal += 1
            else:
                bal -= 1
                if s[i-1] == "(":
                    ans += 2**bal
        return ans



