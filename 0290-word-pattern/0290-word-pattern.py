class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = list(s.split())
        store_pattern = {}
        store_s = {}
        if len(s) != len(pattern):
            return False
        
        for i in range(len(s)):
            if s[i] in store_s:
                if store_s[s[i]] != pattern[i]:
                    return False
            elif pattern[i] in store_pattern:
                if store_pattern[pattern[i]] != s[i]:
                    return False
            else:
                store_s[s[i]] =  pattern[i]
                store_pattern[pattern[i]] = s[i]
            
        
        return True