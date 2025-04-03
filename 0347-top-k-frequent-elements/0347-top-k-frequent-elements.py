class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        arr = []
        for value, count in counts.items():
            arr.append([count, value])
        
        def partition(nums, left, right) :
            random = randint(left,right)
            nums[left], nums[random] = nums[random], nums[left]
            pivot = left

            write = left + 1
            for read in range(left+1, right+1):
                if nums[read] < nums[pivot]:
                    nums[write], nums[read] = nums[read], nums[write]
                    write += 1
            nums[pivot], nums[write - 1] = nums[write-1], nums[pivot]
            return write - 1
        def quickSelect(nums, left, right):
            if left == right:
                return left
            
            pivot = partition(nums,left,right)
            if pivot == len(nums)-k:
                return pivot
            elif pivot > len(nums) - k:
                return quickSelect(nums, left, pivot - 1)
            else:
                return quickSelect(nums, pivot+ 1, right)
        index = quickSelect(arr, 0, len(arr) - 1)
        res = []
        print(arr)
        for i in range(index, len(arr)):
            res.append(arr[i][1])
        return res
            

            
