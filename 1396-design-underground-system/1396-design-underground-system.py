class UndergroundSystem:

    def __init__(self):
        self.passengers = {}
        self.routes = defaultdict(lambda: [0,0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:  
        self.passengers[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.passengers[id]
        route = (startStation, stationName)
        time = t - startTime
        self.routes[route][0] += time
        self.routes[route][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime, travels = self.routes[(startStation, endStation)]
        return totalTime/travels
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)