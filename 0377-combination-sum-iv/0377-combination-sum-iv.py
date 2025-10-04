class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        store = {}

        def dp(summ):
            if summ == target:
                return 1
            if summ > target:
                return 0
            if summ in store:
                return store[summ]
            
            ans = 0
            for num in nums:
                ans += dp(summ + num)
            store[summ] = ans
            return ans
        return dp(0)
        