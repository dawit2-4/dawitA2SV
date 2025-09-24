class Solution:
    def createSortedArray(self, nums: List[int]) -> int:
        MOD = int(1e9 + 7)

        count = defaultdict(lambda : [0, 0])
        def merge(left, right):
            values = [nums[i] for i in left]
            # print(values)
            for z in right:
                idx = bisect_left(values, nums[z])
                # print(nums[z], idx)
                count[z][0] += idx % MOD
                count[z][0] %= MOD
                idx2 = bisect_right(values, nums[z])
                count[z][1] += (len(left) - idx2) % MOD
                count[z][1] %= MOD
            
            i, j = 0, 0
            res = []
            while i < len(left) or j < len(right):
                if j >= len(right) or (i < len(left) and nums[left[i]] < nums[right[j]]):
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            return res
        
        def split(arr,left, right):
            # print(arr, left, right)
            if left == right:
                return [arr[left]]
            mid = (left+right)//2

            sorted_left = split(arr, left, mid)
            sorted_right = split(arr, mid+1, right)
            return merge(sorted_left, sorted_right)
        

        split([i for i in range(len(nums))], 0, len(nums) - 1)
        ans = 0
        # print(count)
        for i in range(len(nums)):
            ans += (min(count[i]) % MOD) 
            ans %= MOD
        return ans % MOD
                