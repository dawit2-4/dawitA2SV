class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort(key=lambda x:x[0])
        ans = []
        time = 0
        n = len(tasks)
        heap = []
        i = 0

        while i < n or heap:
            while i < n and tasks[i][0] <= time:
                enqueue, ptime, idx = tasks[i]
                heapq.heappush(heap,(ptime, idx))
                i += 1
            
            if heap:
                ptime, idx = heapq.heappop(heap)
                ans.append(idx)
                time += ptime

            else:
                time = tasks[i][0]
        return ans
