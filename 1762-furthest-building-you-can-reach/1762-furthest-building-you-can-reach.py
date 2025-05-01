class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        diff = []
        for i in range(1, len(heights)):
            diff.append([heights[i]-heights[i-1], i])
        max_heap = []
        min_heap = []
        last_idx = 0

        for num in diff:
            
            if num[0] >= 0:
                if len(min_heap) < ladders:
                    heappush(min_heap, num[0])
                    last_idx = num[1]
                else:
                    if min_heap and num[0] >= min_heap[0]:
                        if sum(max_heap) + min_heap[0] > bricks:
                            return last_idx
                        else:
                            heappush(max_heap, heappop(min_heap))
                            heappush(min_heap, num[0])
                            last_idx = num[1]
                    else:
                        if sum(max_heap) + num[0] > bricks:
                            return last_idx
                        else:
                            heappush(max_heap, num[0])
                            last_idx = num[1]
            else:
                last_idx = num[1]
        return last_idx