class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        pref = [0,arr[0]]
        for x in arr[1:]:
            pref.append(pref[-1]^x)
        
        count = 0
        for i in range(len(pref)):
            for j in range(i+1, len(pref)):
                if pref[i]^pref[j] == 0:
                    count += j - i - 1
        return count