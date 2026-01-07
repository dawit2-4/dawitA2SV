class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        
        intervals.sort()

        for start, end in intervals:
            if not ans or ans[-1][1] < start:
                ans.append([start, end])
            else:
                ans[-1][1] = max(ans[-1][1], end)
        return ans