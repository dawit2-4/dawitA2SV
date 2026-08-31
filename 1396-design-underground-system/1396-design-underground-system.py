class UndergroundSystem:

    def __init__(self):
        self.cities = defaultdict(list)
        self.passengers = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:  
        self.passengers[id].append([stationName, t])
        if stationName not in self.cities:
            self.cities[stationName] = []
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, time = self.passengers[id][-1]
        cityFound = False
        for route in self.cities[startStation]:
            city, _, _ = route
            if city == stationName:
                route[1] += t - time
                route[2] += 1
                cityFound = True
        if not cityFound:
            self.cities[startStation].append([stationName, t-time, 1])
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        for city, times, number in self.cities[startStation]:
            print(times, number, city)
            if city == endStation:
                
                return times / number
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)