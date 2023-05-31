class UndergroundSystem:

    def __init__(self):
        self.trip_starts = {}
        self.trip_count = collections.defaultdict(int)
        self.trip_times = collections.defaultdict(int) 

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.trip_starts[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.trip_starts[id]
        del self.trip_starts[id]
        trip = (startStation, stationName)
        self.trip_count[trip] += 1
        self.trip_times[trip] += t - startTime

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        trip = (startStation, endStation)
        return self.trip_times[trip]/self.trip_count[trip]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)