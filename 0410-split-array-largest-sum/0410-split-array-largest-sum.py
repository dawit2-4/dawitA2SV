class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)
        
        def validate(val):
            count = 1
            cur_sum = 0

            for num in nums:
                if cur_sum + num > val:
                    cur_sum = num
                    count += 1
                else:
                    cur_sum += num
            return count <= k

        while low <= high:
            mid = (low + high) // 2
            if validate(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

        

