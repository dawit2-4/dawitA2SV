class MedianFinder:

    def __init__(self):
        self.max_hp = []
        self.min_hp = []

    def addNum(self, num: int) -> None:
        max_hp = self.max_hp
        min_hp = self.min_hp

        if not max_hp:
            heappush(max_hp, -num)
            return
        if -max_hp[0] >= num:
            heappush(max_hp, -num)
        else:
            heappush(min_hp, num)
        
        while len(max_hp) > len(min_hp):
            heappush(min_hp, -heappop(max_hp))
        while len(min_hp) - 1 > len(max_hp):
            heappush(max_hp, -heappop(min_hp))
        
        

    def findMedian(self) -> float:
        max_hp = self.max_hp
        min_hp = self.min_hp
       
        if len(min_hp) == len(max_hp):
            med = (-max_hp[0] + min_hp[0]) / 2
        else:
            if min_hp:
                med = min_hp[0]
            else:
                med = -max_hp[0]
            
       
        return med

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
