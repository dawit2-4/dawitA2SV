class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        left_wall = 0
        right_wall = 0

        for i in range(n):
            j = -i - 1
            left_max[i] = left_wall
            right_max[j] = right_wall
            left_wall = max(left_wall, height[i])
            right_wall = max(right_wall, height[j])
        ans = 0
        print(left_max, right_max)
        for i in range(n):
            possible = min(left_max[i], right_max[i])
            ans += max(possible - height[i], 0)
        return ans