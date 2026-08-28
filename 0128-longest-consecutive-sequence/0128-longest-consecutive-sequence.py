class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        max_length = 0
        for num in store:
            if (num - 1) not in store:
                length = 0
                while (num + length) in store:
                    length += 1
                max_length = max(max_length, length)
        return max_length

        
        
        