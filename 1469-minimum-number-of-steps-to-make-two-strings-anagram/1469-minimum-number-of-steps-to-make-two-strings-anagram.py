class Solution:
    def minSteps(self, s: str, t: str) -> int:
        store_s = Counter(s)
        store_t = Counter(t)
        count = 0
        
        for key in store_s:
            if key in store_t:
                if store_s[key] > store_t[key]:
                    count += store_s[key] - store_t[key]
            else:
                count += store_s[key]
            
        return count