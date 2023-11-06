# insert interval

# def insert(intervals, newInterval):
#     if len(intervals) == 0: 
#         return intervals + [newInterval]
#     res = []
#     for z in intervals: 
#         # test if the interval overlaps, if so, absorb it
#         a, b = z
#         if newInterval: 
#             x, y = newInterval
#             if x <= a <= y or x <= b <= y or a < x < y < b:
#                 newInterval = [min(a,x), max(y,b)]  
#         # if it doesn't overlap
#             elif newInterval and a > y: 
#                 res.append(newInterval)
#                 newInterval = None
#                 res.append(z)
#             else:
#                 res.append(z)
#         else:
#             res.append(z)
#     # at the end, if there wasnt an interval after the overlap, append the newinterval
#     if newInterval:
#         res.append(newInterval)
#         newInterval = None
#     return res


intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]

print(insert(intervals, newInterval))

print(insert([[1,5]], [2,3]))
# intervals = [[1,3],[6,9]]
# newInterval = [2,5]

# print(insert(intervals, newInterval))


# intervals = [[6,9]]
# newInterval = [2,5]

# print(insert(intervals, newInterval))




def insert(interval, newInterval):

