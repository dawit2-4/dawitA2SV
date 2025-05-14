class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pref = [0]
        for a in arr:
            pref.append(pref[-1]^a)
        ans = []
        
        
        for q in queries:
            l, r = q
            ans.append(pref[l]^pref[r+1])
        return ans
