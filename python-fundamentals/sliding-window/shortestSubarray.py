from math import inf 
from collections import deque

# Intuition
# define a monotonic deque with increasing prefix; at d[0], we should have the smallest prefix so prefix[i] - prefix[0] is largest
# Note that with the deque, we discard sums that are higher than the one we append because if a lower one works, we dont need to check higher ones because 
# we found one that has higher i that is lower so it will be valid and a lower length.
# Iterate across each i in nums
# We will examine d[0] to see if it's a valid window. If it is valid window, update minLength. If we find d[0] works, we popleft it. 
# We dont ever need to use it again because if we introduce a higher i, we alredy found a lower i that is a valid window.
# 

# Time: O(n) Space: O(n)

def shortestSubarray1(nums, k):    
    d = deque()

    prefixSum = [x for x in nums]
    for i in range(1, len(nums)):
        prefixSum[i] = prefixSum[i] + prefixSum[i-1]

    minLength = inf 
    for i in range(len(prefixSum)):
        if prefixSum[i] >= k: 
            minLength = min(minLength, i + 1)

        # build the monotonic increasing deque         
        while d and prefixSum[d[-1]] > prefixSum[i]: 
            d.pop()
        d.append(i)

        while d and (prefixSum[i] - prefixSum[d[0]] >= k): 
            minLength = min(minLength, i - d[0])
            d.popleft()

    return -1 if minLength == inf else minLength



# nums = [1]
# k = 1

# nums = [1,2]
# k = 4

# nums = [2,-1,2]
# k = 3
#       0  1  2  3   4   5   6   7  8  9  10
# pref [1, 3, 4, 6,  2, -5, -4, -2, 1, 2, 3]
# nums = [1, 2, 1, 2, -4, -7,  1,  2, 3, 1, 1]
# k = 5

# nums = [84,-37,32,40,95]
# k = 167

nums = [17985,-36292,-23941,80618,20594,-6181,9181,65796,-25716,66593,-6873,34062,29878,852,-4767,-36415,11783,8085,-41063,-39940,74284,66272,82385,51634,-48550,9028,-30777,86509,44623,9413,-38369,-1822,46408,35217,72635,-16560,85373,52105,39477,3852,45974,-21593,15481,47280,73889,-42981,54978,95169,-19615,93133]
k = 387303



print(shortestSubarray1(nums, k))