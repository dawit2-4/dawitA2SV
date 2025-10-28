class Solution:
    def minSteps(self, s: str, t: str) -> int:
        store_s = Counter(s)
        store_t = Counter(t)
        count = len(s)
        
        for key in store_s:
            if key in store_t:
                count -= (min(store_s[key], store_t[key]))
            
        return count