class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        s, e = 0, len(nums) - 1
        nums.sort()
        while s < e:
            if nums[s] + nums[e] == k:
                count += 1
                e -= 1
                s += 1
            elif nums[s] + nums[e] > k:
                e -= 1
            else:
                s += 1
        return count
