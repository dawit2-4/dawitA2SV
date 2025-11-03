class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        store = {}
        ans = [1] * n
        dry = SortedList()

        for  i, x in enumerate(rains):
            if x == 0:
                dry.add(i)
            else:
                ans[i] = -1
                if x in store:
                    bs = dry.bisect_left(store[x])
                    if bs == len(dry):
                        return []
                    ans[dry[bs]] = x
                    dry.discard(dry[bs])
                store[x] = i
        return ans