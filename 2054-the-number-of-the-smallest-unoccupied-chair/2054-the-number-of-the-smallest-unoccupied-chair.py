class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        times = sorted([(a, b, i) for i, (a, b) in enumerate(times)])
        hp = [] 
        pos = [i for i in range(len(times))]
        heapify(pos)
        for s, e, i in times:
            while hp and hp[0][0] <= s:
                end, p = heappop(hp)
                heappush(pos, p)
            if targetFriend == i:
                return pos[0]
            heappush(hp, (e, heappop(pos)))

