class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return[]
        p_count = Counter(p)
        s_count = Counter(s[:len(p)])
        result=[]

        if s_count == p_count:
            result.append(0)
        for i in range(len(p), len(s)):
            s_count[s[i]] += 1
            s_count[s[i - len(p)]] -= 1
            if s_count[s[i - len(p)]] == 0:
                del s_count[s[i - len(p)]]
            
            if s_count == p_count:
                result.append(i - len(p) +1)
            
        return result
        # other way
    class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return[]
        pCount, sCount = {}, {}
        for i in range(len(p)):
            pCount[p[i]] = 1 + pCount.get(p[i], 0)
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
        ans = [0] if pCount == sCount else []

        l = 0
        for r in range(len(p), len(s)):
            sCount[s[r]] = 1 + sCount.get(s[r], 0)
            sCount[s[l]] -= 1 
            if sCount[s[l]] == 0:
                sCount.pop(s[l])
            l += 1
            if sCount == pCount:
                ans.append(l)
        return ans
