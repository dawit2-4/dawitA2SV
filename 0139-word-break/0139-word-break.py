class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = wordDict     
        store = {}                   

        def dp(i):
            if i == len(s):          
                return True
            if i in store:           
                return store[i]
            
            
            for word in word_set:
                if s.startswith(word, i):   
                    if dp(i + len(word)):
                        store[i] = True
                        return True
            store[i] = False
            return False

        return dp(0)
