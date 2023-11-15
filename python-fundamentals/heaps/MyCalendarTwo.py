from bisect import bisect_left, bisect
from collections import deque
from math import inf 



# lets do this brute force: N^2


# key for interval: 
# for any two intervals [start, end], [s, e]:
#     if max(start, s) < min(end, e): , then you have the overlap. 

# The overlapped interval is [max(start, s), min(end, e)]

class MyCalendarTwo:

    def __init__(self):
        self.entries = [] # entries sorted by start time
        self.overlaps = []


    def book(self, start, end):
        # check if you hit any overlaps; if so, return False

        for s, e in self.overlaps: 
            if max(start, s) < min(end, e): return False

        # you're good; Now build any overlaps
        for s, e in entries: 
            if max(start, s) < min(end, e): 
                overlap = [max(start, s), min(end, e)]
                self.overlaps.append(overlap)
        # insert to entries
        self.entries.append([start, end])
        return True


# all crap below

# class MyCalendarTwo:

#     def __init__(self):
#         self.entries = [] # entries sorted by start time
#         self.overlaps = []

#     def checkTriples(self, start, end): 
#         idx = bisect(self.overlaps, start, key = lambda x: x[1])
#         if idx < len(self.overlaps):
#             checkStart, checkEnd = self.overlaps[idx]
#             if checkStart < end: 
#                 return False
#         return True

#     def insertOverlap(self, start, end):
#         idx = bisect(self.overlaps, start, key = lambda x: x[1])
#         self.overlaps = self.overlaps[:idx] + [[start, end]] + self.overlaps[idx:]

#     def buildOverlaps(self, start, end):

#         # check overlaps on left
#         idx = bisect_left(self.entries, start, key = lambda x: x[0])
#         leftPossibleOverlaps = self.entries[:idx]
#         leftPossibleOverlaps.sort(key=lambda x: x[1])

#         if leftPossibleOverlaps:
#             i = len(leftPossibleOverlaps) - 1
#             while True:
#                 if 0 <= i < len(leftPossibleOverlaps): 
#                     a, b = leftPossibleOverlaps[i]
#                     if start < b:
#                         self.insertOverlap(start, min(b, end))
#                         i -=1
#                     else: 
#                         break 
#                 else: 
#                     break

#         # check overlaps on right
#         if idx < len(self.entries):
#             a, b = self.entries[idx]
#             if a <  end: 
#                 self.insertOverlap(a, min(b, end))

#     def insertInterval(self, start, end):
#         idx = bisect(self.entries, start, key = lambda x: x[0])
#         self.entries = self.entries[:idx] + [[start, end]] + self.entries[idx:]

#     def book(self, start: int, end: int) -> bool:
#         if self.checkTriples(start, end) == False: 
#             return False

#         # this is a valid entry; 
#         # now build the overlaps
#         self.buildOverlaps(start, end)

#         # then insert interval into entries 
#         self.insertInterval(start, end)
#         return True

# start, end = [12,13]
# arr = [[3,4], [5,7]]
# idx = bisect(arr, start, key = lambda x: x[1])
# a, b = arr[idx]
# print( a < end)



cal = MyCalendarTwo()
# cal.book(3,6)
# cal.book(1,4)
# cal.book(-1,2)
# print(cal.book(3,5))
# arr = [[10,20],[50,60],[10,40],[5,15],[5,10],[25,55]]

arr = [[69,78],[81,86],[80,87],[58,66],[40,46],[81,88],[40,47],[18,25],[52,59],[80,88],[58,63],[15,21],[79,87],[77,83],[9,14],[67,76],[39,44],[36,45],[11,20],[61,69],[51,60],[49,57],[48,53],[2,8],[8,15],[49,57],[8,16],[42,51],[94,100],[44,50],[1,9],[69,78],[47,53],[98,100],[56,62],[26,31],[3,9],[68,75],[85,92],[52,57],[51,59],[18,26],[60,65],[92,99],[90,98],[89,97],[39,44],[31,39],[90,96],[44,49],[44,49],[47,54],[24,32],[59,68],[29,34],[38,43],[3,8],[98,100],[48,57],[19,24],[65,71],[20,29],[18,23],[67,76],[78,86],[43,48],[30,39],[49,56],[48,56],[84,91],[13,18],[96,100],[31,36],[1,8],[90,97],[96,100],[20,28],[45,52],[1,6],[13,22]]
def runCal(arr):
    res = []
    print(len(arr))
    for i, (start, end) in enumerate(arr):
        if i < 80 -8 :
            print(start, end)
            res.append(cal.book(start, end))

    print("entries: ", cal.entries, "overlaps: ", cal.overlaps)
    print(res)
    return res

runCal(arr)

# arr = []
# cal = MyCalendarTwo()
# print(cal.book(10, 20))
# print(cal.book(10, 20))
# print(cal.book(10, 20))
# print(cal.book(30, 50))
# print(cal.book(40, 70))
# print(cal.book(55, 72))
# print(cal.book(155, 172))
# print(cal.book(156, 172))
# print(cal.book(157, 172))
# print(cal.entries)

# for start, end in [[10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]:
#     print(cal.book(start, end))


# arr = [[69,78],[81,86],[80,87],[58,66],[40,46],[81,88],[40,47],[18,25],[52,59],[80,88],[58,63],[15,21],[79,87],[77,83],[9,14],[67,76],[39,44],[36,45],[11,20],[61,69],[51,60],[49,57],[48,53],[2,8],[8,15],[49,57],[8,16],[42,51],[94,100],[44,50],[1,9],[69,78],[47,53],[98,100],[56,62],[26,31],[3,9],[68,75],[85,92],[52,57],[51,59],[18,26],[60,65],[92,99],[90,98],[89,97],[39,44],[31,39],[90,96],[44,49],[44,49],[47,54],[24,32],[59,68],[29,34],[38,43],[3,8],[98,100],[48,57],[19,24],[65,71],[20,29],[18,23],[67,76],[78,86],[43,48],[30,39],[49,56],[48,56],[84,91],[13,18],[96,100],[31,36],[1,8],[90,97],[96,100],[20,28],[45,52],[1,6],[13,22]]

# for i, [start, end] in enumerate(arr):
#     if i < 31: 
#         print(cal.book(start, end), (start, end))

# arr = [[12,26],[70,85],[55,67],[2,13],[3,18],[91,100],[13,26],[17,27],[41,55],[15,26],[50,68],[34,52],[95,100],[23,33],[89,100],[27,43],[80,95],[97,100],[28,47],[45,58],[76,93],[56,75],[91,100],[61,77],[36,49],[18,32],[96,100],[96,100],[67,86],[46,64],[95,100],[17,35],[8,27],[4,14],[30,43],[74,89],[77,95],[98,100],[31,41],[35,53]]
# for i, [start, end] in enumerate(arr):
#     if i < 11: 
#         print(cal.book(start, end), (start, end))

# print(cal.entries)