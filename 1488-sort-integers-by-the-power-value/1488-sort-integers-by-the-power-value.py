class Solution:
    def helper(self,num):
        count = 0
        while num !=1:
            if num % 2 == 0:
                num = num / 2
            else:
                num = (3 * num) + 1
            count += 1
        return count
    def getKth(self, lo: int, hi: int, k: int) -> int:
        ans = []
        for i in range(lo, hi+1):
            val = self.helper(i)
            ans.append((val, i))
        ans.sort()
        return ans[k-1][1]