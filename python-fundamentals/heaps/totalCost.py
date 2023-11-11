
# https://leetcode.com/problems/total-cost-to-hire-k-workers/?envType=daily-question&envId=2023-11-10

from collections import deque
from heapq import heappush, heappop

# - Boundaries represent what is included and we'll use it to decide when 
#   we we choose a worker, which side we'll push into the queue
# - first we'll push from 0 to left boundary and from right to end of costs into a priority queue
# - and we'll use heappush(queue, (val, i)) so that in case of ties of val, the lower ith gets chosen
# - we'll iterate k times: 
#       - pop an item
#       - record the cost to totalcost
#       - if left boundary < rightBoundary then add another one into the queue:
#       - if index < left boundary, then increase boundary by one, and then pop the next 
#       - otherwise, add the right boundary

# I rewrote this to use a deque because I'm not great with indeces tracking and I need to be super careful. 

def totalCost(costs, k, candidates):
    totalCost = 0
    dequeCandidates = deque([(val, i) for i, val in enumerate(costs)])
    queue = []

    for _ in range(candidates):
        if dequeCandidates:
            val, idx = dequeCandidates.popleft()
            heappush(queue, (val, idx))
        if dequeCandidates:
            val, idx = dequeCandidates.pop()
            heappush(queue, (val, idx))
    
    for _ in range(k):
        val, idx = heappop(queue)
        totalCost += val
        if dequeCandidates: 
            if idx < dequeCandidates[0][1]:
                newCost, newIdx = dequeCandidates.popleft()
            else: 
                newCost, newIdx = dequeCandidates.pop()
            heappush(queue, (newCost, newIdx))
    return totalCost

# costs = [1,2,4,1]
# k = 3
# candidates = 3


# costs = [17,12,10,2,7,2,11,20,8]
# k = 3
# candidates = 4


costs = [18,64,12,21,21,78,36,58,88,58,99,26,92,91,53,10,24,25,20,92,73,63,51,65,87,6,17,32,14,42,46,65,43,9,75]
print(len(costs))
k = 13
candidates = 23
# 223

costs = [31,25,72,79,74,65,84,91,18,59,27,9,81,33,17,58]
k = 11 
candidates = 2

print(totalCost(costs, k, candidates))