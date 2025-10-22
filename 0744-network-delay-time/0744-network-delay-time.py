class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        mat = defaultdict(list)
        
        for s, e, t in times:
            mat[s].append((e,t))
        dist = {}
        heap = [(0,k)]
        
        while heap:
            time, node = heappop(heap)
            if node in dist:
                continue
            
            dist[node] = time
            for nei, w in mat[node]:
                if nei not in dist:
                    heappush(heap, (time+w, nei))
        if len(dist) < n:
            return -1
        
        return max(dist.values())