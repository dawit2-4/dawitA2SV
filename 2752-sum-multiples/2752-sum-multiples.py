class Solution:
    def sumOfMultiples(self, n: int) -> int:
        ans = 0
        for i in range(n+1):
            if i % 3 == 0 or i % 7 == 0 or i % 5 == 0:
                ans += i
        return ans