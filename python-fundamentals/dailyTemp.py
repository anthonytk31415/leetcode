

from bisect import bisect_left, bisect
from math import inf

# n log n algorithm

# keep a sorted array of temperatures where arr[i] = (temp, index in original)

# you'll iterate on x (from right to left of the orignal array)

# for each x, find the index where you will insert the new element in the array; 


# when looking for the next highest temp (ie. finding z ) in the sort temp array, you want to grab the earliest one 
# 
from collections import deque

def dailyTemperatures(temp):
    processed = [0]*len(temp)
    stack = deque()

    for i, t in enumerate(temp):
        while stack and temp[stack[-1]] < t: 
            i_cur = stack.pop()
            processed[i_cur]= i - i_cur
        stack.append(i)
        
    return processed    

    # dailyTemperatures(self, T):
    # ans = [0] * len(T)
    # stack = []
    # for i, t in enumerate(T):
    #   while stack and T[stack[-1]] < t:
    #     cur = stack.pop()
    #     ans[cur] = i - cur
    #   stack.append(i)

    # return ans


temp = [73,74,75,71,69,72,76,73]
print( dailyTemperatures(temp))