class Solution:
    def minSteps(self, s: str, t: str) -> int:
        store_s = defaultdict(int)
        store_t = defaultdict(int)
        count = len(s)

        for i in range(len(s)):
            store_s[s[i]] += 1
            store_t[t[i]] += 1
        
        for key in store_s:
            if key in store_t:
                count -= (min(store_s[key], store_t[key]))
            
        return count