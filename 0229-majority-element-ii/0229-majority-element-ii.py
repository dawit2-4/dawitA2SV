class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        ans = []
        n = len(nums)

        for key, val in c.items():
            if val > math.floor(n/3):
                ans.append(key)
        
        return ans