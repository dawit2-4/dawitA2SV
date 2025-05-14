class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans = [0] * len(pref)
        for i in range(1, len(pref)):
            ans[i] = pref[i] ^ pref[i-1]
        ans[0] = pref[0]
        return ans
