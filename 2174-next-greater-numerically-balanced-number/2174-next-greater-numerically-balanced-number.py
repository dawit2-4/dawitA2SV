class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        for i in range(n+1, 1224444+1):
            c = Counter(str(i))
            flag = True
            for key, val in c.items():
                if int(key) != val:
                    flag = False
                    break
            if flag:
                return i
