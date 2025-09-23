class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        half = sum(nums) // 2

        from functools import lru_cache

        @lru_cache(None)
        def rec(end, summ):
            if end < 0:
                return False
            if summ == half:
                return True
            if summ > half:
                return False
            

            #Take
            cur = summ + nums[end]
            take = rec(end - 1, cur)
            if take:
                return take

            #Not Take
            notTake = rec(end - 1, summ)

            return notTake or take
        return rec(len(nums)-1, 0)
