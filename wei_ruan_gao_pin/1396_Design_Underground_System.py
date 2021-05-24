class UndergroundSystem:

    def __init__(self):
        self.dict = collections.defaultdict(list)
        self.ongoing = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.ongoing[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.ongoing[id]
        self.dict[(startStation, stationName)].append(t-startTime)
        del self.ongoing[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.dict[(startStation,endStation)]) / len(self.dict[(startStation,endStation)])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
