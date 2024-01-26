from bisect import bisect_left
from itertools import accumulate

def changeArray(arr, num):
    arr.sort()
    prefix = list(accumulate(arr))
    idx = bisect_left(arr, num)
    numIncrements = 0
    n = len(arr)
    if idx >= n or idx == 0: 
        numIncrements = abs(prefix[n-1] - n*num)
    else: 
        numIncrements = abs(prefix[n-1] - prefix[idx - 1] - (n-1-idx+1)*num) + abs(prefix[idx-1] - (idx)*num)

    return numIncrements 


arr = [1,3,2,4,7]
num = 10
print(changeArray(arr, num))