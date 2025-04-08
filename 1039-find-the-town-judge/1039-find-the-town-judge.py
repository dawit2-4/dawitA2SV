class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        in_degree = [0] * n
        out_degree = [0] * n

        for person , t in trust:
            out_degree[person - 1] += 1
            in_degree[t-1] += 1
        for i in range(n):
            if out_degree[i] == 0 and in_degree[i] == n - 1:
                return i + 1
        return -1

