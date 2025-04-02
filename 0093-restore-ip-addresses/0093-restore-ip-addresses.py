class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        path = []

        def backtrack(start):
            if len(path) == 4:
                if start == len(s):
                    ans.append('.'.join(path))
            
            for i in range(1,4):
                if i + start > len(s):
                    break
                portion = s[start:start+i]
                if (portion[0] == '0' and len(portion) > 1) or int(portion) > 255:
                    continue
                path.append(portion)
                backtrack(start+i)
                path.pop()

        backtrack(0)
        return ans