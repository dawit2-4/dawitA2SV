class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def checker(i):
            l = 0
            arr = [0] * len(nums)
            while l <= i:
                left = queries[l][0]
                right = queries[l][1]
                val = queries[l][2]
                arr[left] -= val
                if right+1 < len(arr):
                    arr[right+1] += val
                l += 1

            if arr[0] + nums[0] > 0:
                return False
            for j in range(1,len(arr)):
                arr[j] += arr[j-1]
                if arr[j] + nums[j] > 0:
                    return False
            return True

        low = -1
        high = len(queries) - 1

        while low <= high:
            mid = (low+high)//2
            if checker(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low + 1 if low < len(queries) else -1
