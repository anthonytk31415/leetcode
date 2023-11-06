
# 1:59
def merge(intervals):
    intervals.sort(key = lambda x: x[0])
    index = 0
    for i in range(1, len(intervals)):
        print(f'i = {i}, index = {index}')
        if intervals[index][1] >= intervals[i][0]:
            intervals[index][1] = max(intervals[index][1], intervals[i][1])
        else: 
            index +=1
            intervals[index] = intervals[i]
        
    return intervals[:index+1]

# intervals  = [[1,3],[2,6],[8,10],[15,18]]
# 
intervals = [[1,4],[0,2],[3,5]]
print(merge(intervals))