from heapq import heappush, heappop
from math import inf 

# use a priority queue. 
# apparently you could solve this with DP


#Time: O(nlogn); Space: O(n) for the queue;

def findLongestChain(pairs):
    queue = []
    for pair in pairs:
        beg, end = pair
        heappush(queue, (end, beg))

    counter = 0
    priorEnd = -inf
    while queue: 
        cur = heappop(queue)
        curEnd, curBeg = cur
        if curBeg > priorEnd: 
            counter +=1
            priorEnd = curEnd
    return counter

# pairs = [[1,2],[2,3],[3,4]]
pairs = [[1,2],[7,8],[4,5]]
print(findLongestChain(pairs))