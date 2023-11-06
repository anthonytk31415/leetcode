from collections import deque
def removeCoveredIntervals(intervals): 
    intervals.sort(key = lambda x: (x[0], -x[1]))
    covered = 0
    last = -1
    for x in intervals: 
        if x[1] <= last:
            covered +=1
        else: 
            last = x[1]
    return len(intervals) - covered