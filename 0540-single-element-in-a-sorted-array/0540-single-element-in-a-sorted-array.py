class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n= len(nums)
        left = 0
        right = n - 1
        if n == 1:
            return nums[0]
        
        while True:
            mid = (left + right) // 2
            if mid == 0 or mid == n - 1: return nums[mid]
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid+1]:
                return nums[mid]
            if (mid - left) % 2 != 0:
                if nums[mid] != nums[mid - 1]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] != nums[mid - 1]:
                    left = mid + 2
                else:
                    right = mid - 2
        
                
        
                    