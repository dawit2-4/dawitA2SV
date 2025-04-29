import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k

        heapq.heapify(self.nums)
    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        
        while self.k < len(self.nums):
            # for _ in range(self.k):
                largest = heapq.heappop(self.nums)
        # else:
        #     largest = heapq.heappop(self.nums)
        # heapq.heappush(self.nums, largest)
        return self.nums[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
