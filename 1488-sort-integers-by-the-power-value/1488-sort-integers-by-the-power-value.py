class Solution:
    def helper(self, num):
        count = 0
        while num != 1:
            if num % 2 == 0:
                num //= 2
            else:
                num = (num*3) + 1
            count += 1
        return count

    def getKth(self, lo: int, hi: int, k: int) -> int:
        ans = []
        for i in range(lo, hi+1):
            count = self.helper(i)
            ans.append((count, i))
        ans.sort()
        # print(ans)
        return ans[k-1][1]