class Solution:
    def countVowels(self, word: str) -> int:
        vowels = ['a', 'e', 'i','o', 'u']
        store = []
        n = len(word) 


        for i in range(n):
            if word[i] in vowels:
                store.append(i)
        
        count = 0
        for v in store:
            before = v + 1
            after = n - v
            
            count += (before * after)
        return count
