# k closestto x

# take abs x - z in arr
# find the first index of min(arr)

from collections import deque

def findClosestElements(arr, k, x):
    delta = [abs(x - z) for z in arr]
    idx = delta.index(min(delta))
    i, j= idx - 1, idx + 1
    res = deque()
    res.append(arr[idx])
    while i >= 0 and j < len(arr) and len(res) < k: 
        print(i, j, k)
        if delta[i] <= delta[j]:
            res.appendleft(arr[i])
            i -=1
        elif delta[i] > delta[j]:
            res.append(arr[j])
            j +=1
    while i >= 0 and len(res) < k: 
        res.appendleft(arr[i])
        i -=1
    while j < len(arr) and len(res) < k: 
        res.append(arr[j])
        j +=1
    return list(res)

# arr = [1,2,3,4,5]
# k = 4
# x = 3

# arr = [-2,-1,1,2,3,4,5]
# k = 7
# x = 3
# >> [-2,-1,1,2,3,4,5]

arr = [0,0,1,2,3,3,4,7,7,8]
k = 3
x = 5
print(findClosestElements(arr, k, x))