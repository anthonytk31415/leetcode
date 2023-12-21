# Straightforward use of binary search. First create a starts array that's sorted and a way to retrieve it's original index in O(1)
# time using a hash table. 
# Then for each interval, bisect the end_i to find the smallest start_j s.t. end_i <= start_j. 
# if that index is larger than your starts, then append -1 to the res. Otherwise, append that index. 
# Return the res

# Time: O(nlogn) for sorts and bisect_left (binary search)
# Space: O(N) for the result and the start to index lookup as well as a nice, convenient starts array; could be optimized a bit

from bisect import bisect_left
def findRightInterval(intervals):
    startToIdx = {}
    starts = []
    for i, interval in enumerate(intervals):
        start, end = interval
        starts.append(start)
        startToIdx[start] = i
    starts.sort()
    res = []
    for i, interval in enumerate(intervals):
        start, end = interval 
        bisectIdx = bisect_left(starts, end)
        if bisectIdx < len(starts):
            start_j = starts[bisectIdx]            
            start_j_idx = startToIdx[start_j]
            res.append(start_j_idx)
        else: res.append(-1)
    return res

intervals = [[1,4],[2,3],[3,4]]
print(findRightInterval(intervals))