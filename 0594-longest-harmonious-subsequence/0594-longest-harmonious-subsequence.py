class Solution:
    def findLHS(self, nums: List[int]) -> int:
        ans = 0
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        for num in set(nums):
            if count[num+1]:
                c = count[num] + count[num+1]
                ans = max(c, ans)
        return ans