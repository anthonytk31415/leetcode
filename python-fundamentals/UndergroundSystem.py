from collections import defaultdict

class UndergroundSystem:

    class RideSpecs: 
        def __init__(self, id=None, time=None, stationName=None):
            self.time = time
            self.id = id
            self.startDestination = stationName

        def __str__(self):
            return f"ID: {self.id}, StartTime: {self.time}, StartDest: {self.startDestination} "

    class RideTimes:
        def __init__(self):
            self.sumTimes = 0 
            self.count = 0

    def __init__(self):
        self.rides = defaultdict(self.RideSpecs)
        self.times = defaultdict(self.RideTimes)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.rides[id] = self.RideSpecs(id, t, stationName)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        key = f"{self.rides[id].startDestination},{stationName}"
        totalTime = t - self.rides[id].time

        self.times[key].sumTimes += totalTime
        self.times[key].count += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = f"{startStation},{endStation}"
        if key in self.times: 
            return self.times[key].sumTimes / self.times[key].count
        else: 
            return 0


# x = ["UndergroundSystem","checkIn","checkOut","getAverageTime","checkIn","checkOut","getAverageTime","checkIn","checkOut","getAverageTime"]
# y = [[],[10,"Leyton",3],[10,"Paradise",8],["Leyton","Paradise"],[5,"Leyton",10],[5,"Paradise",16],["Leyton","Paradise"],[2,"Leyton",21],[2,"Paradise",30],["Leyton","Paradise"]]

ug = UndergroundSystem()
ug.checkIn(10,"Leyton",3)
print(ug.rides[10])
ug.checkOut(10,"Paradise",8)
print(ug.getAverageTime("Leyton","Paradise"))
ug.checkIn(5,"Leyton",10)
ug.checkOut(5,"Paradise",16)
print(ug.getAverageTime("Leyton","Paradise"))