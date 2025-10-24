class UndergroundSystem:

    def __init__(self):
        self.person = {}
        self.station = {}


    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.person[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, time = self.person[id]
        r = (start, stationName)
        if r not in self.station:
            self.station[r] = [0, 0]
        self.station[r][0] += t - time
        self.station[r][1] += 1


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        r = (startStation, endStation)
        time, count = self.station[r]
        return time / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)