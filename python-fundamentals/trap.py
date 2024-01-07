from heapq import heappush, heappop 
from math import inf 

# The trick is to see that for each i, you require maxLeft so far and maxRight so far

# Time O(n)
# O(n) Space

def trap(height):
    maxLeft, maxRight = [x for x in height], [x for x in height]

    for i in range(1, len(maxLeft)):
        maxLeft[i] = max(maxLeft[i], maxLeft[i-1])

    for i in range(len(maxRight)-2, -1, -1):
        maxRight[i] = max(maxRight[i], maxRight[i+1])

    res = 0
    for i in range(1, len(height)-1):
        res += max(0, min(maxLeft[i-1], maxRight[i+1]) - height[i])

    return res



height = [0,1,0,2,1,0,1,3,2,1,2,1]
# height = [4,2,0,3,2,5]
# height = [5,4,1,2]
print(trap(height))