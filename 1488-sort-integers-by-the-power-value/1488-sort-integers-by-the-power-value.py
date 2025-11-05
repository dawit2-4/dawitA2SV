class Solution:
    @cache
    def helper(self,num):
        if num == 1:
            return 0
        if num % 2 == 0:
            return 1+self.helper(num /2)
        else:
            return 1+self.helper((3*num)+1)
    def getKth(self, lo: int, hi: int, k: int) -> int:
        ans = []
        for i in range(lo, hi+1):
            val = self.helper(i)
            ans.append((val, i))
        ans.sort()
        return ans[k-1][1]