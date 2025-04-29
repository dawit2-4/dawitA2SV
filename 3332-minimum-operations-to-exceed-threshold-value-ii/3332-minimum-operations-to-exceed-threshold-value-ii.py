class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        steps = 0
        while nums[0] < k:
            num1 = heappop(nums)
            num2 = heappop(nums)
            val = (num1*2) + num2

            heappush(nums, val)
            steps += 1
        return steps