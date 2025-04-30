class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        arr = []

        for i in range(len(grid)):
            for num in grid[i]:
                arr.append((-num,i))
        ans = 0
        
        heapify(arr)
        
        while k > 0:
            x, i = heappop(arr)
            x = -x
            
            if limits[i] > 0:
                ans += x
                limits[i] -= 1
                k -= 1
            
            
        return ans