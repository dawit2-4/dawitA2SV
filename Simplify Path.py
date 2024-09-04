class Solution:
    def simplifyPath(self, path: str) -> str:
        p = path.split("/")
        p = [a for a in p if a != ""]

        stack = []
        for a in p:
            if a == ".":
                continue
            elif a == "..":
                if stack: stack.pop()
            else:
                stack.append(a)
        return"/"+"/".join(stack)
