class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            sum_ = 0
            while i > 0:
                sum_ += i%2
                i = i//2
            ans.append(sum_)
        return ans