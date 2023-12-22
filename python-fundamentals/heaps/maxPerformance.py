from heapq import heappush, heappop
from math import inf 

# use a min heap. 

def maxPerformance(n, speed, efficiency, k):
    stats = [[x, y] for x, y in zip(speed, efficiency)]
    stats.sort(key = lambda x: -x[1])
    minHeap = []
    maxPerf = -inf
    sumSpeed = 0
    for x, y in stats: 
        heappush(minHeap, x)
        sumSpeed += x
        if len(minHeap) > k: 
            sumSpeed -= heappop(minHeap)

        maxPerf = max(maxPerf, sumSpeed * y)
    return maxPerf % (10**9 + 7)

# n = 6 
# speed = [2,10,3,1,5,8]
# efficiency = [5,4,3,9,7,2]
# k = 2

# n = 6
# speed = [2,10,3,1,5,8]
# efficiency = [5,4,3,9,7,2]
# k = 3

n = 3
speed = [2,8,2]
efficiency = [2,7,1]
k = 2
print(maxPerformance(n, speed, efficiency, k))