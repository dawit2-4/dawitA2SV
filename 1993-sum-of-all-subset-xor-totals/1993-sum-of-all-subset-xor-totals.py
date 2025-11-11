class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets = []
        def back(i, arr):
            if i >= len(nums):
                subsets.append(arr[:])
                return
            arr.append(nums[i])
            back(i+1, arr)
            arr.pop()
            back(i+1, arr)
        back(0, [])
        result = 0
        for subset in subsets:
            new_xor = 0
            for num in subset:
                new_xor ^= num
            result += new_xor

        return result
