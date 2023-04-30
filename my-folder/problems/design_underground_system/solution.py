class UndergroundSystem:

    def __init__(self):
        self.enroute = {}
        self.times_count = defaultdict(int)
        self.times_total = defaultdict(int)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.enroute[id] = (stationName, t)
        

    def checkOut(self, id: int, endStation: str, endTime: int) -> None:
        startStation, startTime = self.enroute[id]
        route = (startStation, endStation)
        self.times_count[route] += 1
        self.times_total[route] += endTime - startTime

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route = (startStation, endStation)
        return self.times_total[route]/self.times_count[route]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)