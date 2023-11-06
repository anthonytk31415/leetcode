# kadane 

# the max sum subarray is for a[i] is the max sum subarray for a[i-1] + (include or exclude a[i])




-1,3,4,

from math import inf 

def maxSumSubarray(arr):
    cur_max = -inf
    last = False
    for i in range(len(arr)):
        if last == False: 
            cur_max = max([cur_max, arr[i]])
            if cur_max == arr[i]: 
                last = True
        else:
            options = [cur_max + arr[i], arr[i], cur_max]
            cur_max = max(options)
            if cur_max == options[2]:
                last = False
    return cur_max

arr = -4, -3, 5, 4, 3, -12, 15, -38, 2, 3, 