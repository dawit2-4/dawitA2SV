class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        previous_end = 0
        for start, end  in meetings:
            start = max(start, previous_end + 1)
            length = end - start + 1
            days -= max(length, 0)
            previous_end = max(previous_end, end)
        return days
