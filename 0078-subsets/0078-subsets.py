class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        x = 2**n
        ans = []
        for i in range(x):
            temp = []
            b = bin(i)[2:]
            for k in range(n):
                if (1 << k) & int(b) != 0:
                    temp.append(nums[k])
            ans.append(temp)
        return ans