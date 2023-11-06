# 2:14
def insert(intervals, newInterval):
    if len(intervals) == 0: 
        return [newInterval]
    #set i to where the newInterval should be spliced into; i + 1 is where it needs to go
    i = 0
    while True:
        if i >= len(intervals) or intervals[i][0] > newInterval[0]:
            break
        else: 
            i +=1
    intervals = intervals[:i] + [newInterval] + intervals[i:]
    i-=1                # set the pointer to one right before where you inserted, or to 0 if the newInterval is the first in the sorted order
    i = max(0, i)
    # code this part like "interval insertion"
    for j in range(i+1, len(intervals)):
        if intervals[i][1] >= intervals[j][0]:
            intervals[i][1] = max(intervals[i][1], intervals[j][1])
        else:
            i +=1
            intervals[i] = intervals[j]
    return intervals[:i+1]

# intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
# intervals = [[1,2]]
# intervals = [[1,5]]
# newInterval = [0,3]
intervals = [[1,1]]
newInterval = [4,8]
print(insert(intervals, newInterval))