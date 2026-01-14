class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        store = defaultdict(int)

        for i in range(len(nums)):
            if nums[i] in store:
                if i - store[nums[i]] <= k:
                    return True
            store[nums[i]] = i
        
        return False

        