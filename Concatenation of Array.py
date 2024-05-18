class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums+nums


# or

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mylist = [0] * (2*n)

        for i in range(n):
            mylist[i] = nums[i]
            mylist[i+n] = nums[i]
        return mylist
