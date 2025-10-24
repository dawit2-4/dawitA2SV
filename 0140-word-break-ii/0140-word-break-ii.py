class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {}
        ans = []
        def dp(st, arr):
            if len(st) >= len(s) and s != st:
                return False
            if len(st) == len(s) and st == s:
                ans.append(arr)
                return True
            
            val = (st, tuple(arr))
            if val in memo:
                return memo[val]
            validity = False
            for i in range(len(wordDict)):
                if s.startswith(st+ wordDict[i]):
                    new_arr = arr + [i]
                    take = dp(st+wordDict[i], new_arr)
                    validity |= take
            if st and arr:
                memo[val] = validity
            if val != ('', ()):
                return memo[val]
            else:
                return True
        x = dp("", list())
        result = []
        for a in ans:
            temp = ''
            for i in a:
                temp += (wordDict[i])
                temp += " "

            result.append(temp.rstrip())
        return result
            
            
                
            