from math import inf 
from collections import deque

def shortestSubarray1(nums, k):

    # given left and right, find the inclusive sum of nums from left to right
    
    # define a monotonic deque with increasing prefix; iterate across each i in nums
    # and for each right, we will examine d[0] to see if it's a valid window. 
    # if it is, we mark it and then pop it and keep doing so until we cannot pop/not a valid window
    d = deque()

    prefixSum = [x for x in nums]
    for i in range(1, len(nums)):
        prefixSum[i] = prefixSum[i] + prefixSum[i-1]

    minLength = inf 
    for i in range(len(prefixSum)):

        # build the monotonic increasing deque         
        while d and prefixSum[d[-1]] < prefixSum[i]: 
            d.pop()
        d.append(i)

        print(d)

        while d and prefixSum[i] - prefixSum[d[0]] >= k:  
            minLength = min(minLength, i - d[0] + 1)
            d.popleft()

    return -1 if minLength == inf else minLength

# mid to right will be all positive
# left to right will contain all positives and negatives

# when we find a valid array, we'll shrink it at least to mid no matter what. 
# and then after mid, we'll stop if decreasing makes sum < k 
# when we restart the cycle, we'll pick up at mid 

# def shortestSubarray(nums, k):
    # left, right, curSum, mid = 0, 0, 0, 0
    # minLength = inf
    # while right < len(nums):
    #     curSum += nums[right]
    #     if nums[right] < 0: 
    #         mid = right + 1
    #     if curSum < 0: 
    #         curSum, mid, left = 0, right + 1, right + 1
    #     elif curSum >= k:
    #         for i in range(left, mid):




    #         # at the end, left = mid = max(left, mid)


    #     right += 1
    # if minLength == inf: 
    #     return -1
    # return minLength



nums = [1]
k = 1

# nums = [1,2]
# k = 4

# nums = [2,-1,2]
# k = 3

# nums = [1, 2, 1, 2, -4, -7, 1, 2, 3, 1, 1]
# k = 5

# nums = [84,-37,32,40,95]
# k = 167

# nums = [17985,-36292,-23941,80618,20594,-6181,9181,65796,-25716,66593,-6873,34062,29878,852,-4767,-36415,11783,8085,-41063,-39940,74284,66272,82385,51634,-48550,9028,-30777,86509,44623,9413,-38369,-1822,46408,35217,72635,-16560,85373,52105,39477,3852,45974,-21593,15481,47280,73889,-42981,54978,95169,-19615,93133]
# k = 387303



print(shortestSubarray1(nums, k))