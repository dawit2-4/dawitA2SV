class UndergroundSystem:

    def __init__(self):
        self.person = {}
        self.station = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.person[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, time = self.person[id]
        self.station[start].append((start, stationName, t - time))

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        count = 0
        ans = 0
        for t in self.station[startStation]:
            start, end, time = t
            if end == endStation:
                ans += time
                count  += 1
        return ans / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)