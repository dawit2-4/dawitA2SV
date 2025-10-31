class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        store = defaultdict(int)
        store[0] = 1
        running = 0
        for i in range(len(nums)):
            running += nums[i]
            count += store[running-k]
            store[running] += 1
        return count
