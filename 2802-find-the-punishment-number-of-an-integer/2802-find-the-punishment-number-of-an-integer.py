class Solution:
    def punishmentNumber(self, n: int) -> int:
        def can_partition(sqrt_string, i):
            def dfs(index, cur_sum):
                if index == len(sqrt_string):
                    return cur_sum == i
                
                for j in range(index + 1, len(sqrt_string) + 1):
                    num = int(sqrt_string[index:j])
                    if dfs(j, cur_sum + num):
                        return True
                return False
            return dfs(0,0)
        ans = 0
        for i in range(1, n + 1):
            sqrt_string = str(i*i)
            if can_partition(sqrt_string, i):
                ans += i * i
        return ans