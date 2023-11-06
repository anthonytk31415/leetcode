# 1,2

from math import inf

intervals = [[1,2],[2,3],[3,4],[1,3]]

def eraseOverlapIntervals(intervals):
    end = -inf 
    cnt = 0 

    # sort by end; youl'l want to keep the intervals with the shortest end as this will have the least capacity to hold other intervals 
    for s,e in sorted(intervals, key=lambda x: x[1]):
        if s >= end:            # if condition holds, then interval does not overlap (due also with the sort)
            end = e             
        else: 
            cnt +=1             # if they overlap, then you identified an interval you need to toss

    return cnt 
# 1,2; 1,3; 2,3; 3,4
# end = 2; 
# 1,3 > no; 
# cnt > 1
# 2,3 > yes > end = 3
# 3,4: yes > end = 4



# intervals = [[1,2],[1,2],[1,2]]
print(eraseOverlapIntervals(intervals))