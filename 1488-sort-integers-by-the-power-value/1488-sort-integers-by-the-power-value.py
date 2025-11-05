class Solution:
    @cache
    def helper(self,num, count):
        if num == 1:
            return count
        if num % 2 == 0:
            return self.helper(num /2, count +1)
        else:
            return self.helper((3*num)+1, count+1)
    def getKth(self, lo: int, hi: int, k: int) -> int:
        ans = []
        for i in range(lo, hi+1):
            val = self.helper(i, 0)
            ans.append((val, i))
        ans.sort()
        return ans[k-1][1]