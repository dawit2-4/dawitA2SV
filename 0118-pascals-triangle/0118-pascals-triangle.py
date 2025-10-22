class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1]]
        for i in range(1, numRows):
            prev = dp[-1]
            
            row = [1] + [prev[j] + prev[j + 1] for j in range(len(prev) - 1)] + [1]
            dp.append(row)
        return dp
