class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        # count the frequency on numbers in num
        counts = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]

        #store the nums in freq based on their frequency
        for value, count in counts.items():
            bucket[count].append(value)
        
        n = len(bucket)
        print(bucket)

        for i in range(n-1, 0, -1):
            for num in bucket[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
      

            
