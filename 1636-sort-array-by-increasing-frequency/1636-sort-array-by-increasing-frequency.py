class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        store = Counter(nums)
        sorted_store = sorted(store.items(), key= lambda x:(x[1], -x[0]))
        ans = []
        for key, val in sorted_store:
            for _ in range(val):
                ans.append(key)
        return ans