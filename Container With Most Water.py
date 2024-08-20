class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        l, r = 0, len(height) -1
        while l < r:
            calc = min(height[l], height[r]) * (r-l)
            ans = max(ans,calc)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return ans
