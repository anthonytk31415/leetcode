from bisect import bisect_left
from math import inf 

# binary earch. pretty tricky

def findBestValue(arr, target):

    def sumTransformation(num):
        if num < arr[0]: return len(arr) * num
        idx = bisect_left(arr, num)
        res = ((len(arr) - 1) - (idx) + 1)*num
        if idx > 0: res += prefix[idx - 1]
        return res

    arr.sort()
    prefix = [x for x in arr]

    for i in range(1, len(arr)):
        prefix[i] = prefix[i] + prefix[i-1]

    left = 0
    right = arr[-1]
    while left <= right: 
        mid = (left + right )//2
        curSum = sumTransformation(mid)

        if curSum < target: 
            left = mid + 1

        elif curSum > target: 
            right = mid - 1
        else: return mid

    leftDelta = abs(sumTransformation(left) - target)
    rightDelta = abs(sumTransformation(right) - target)
    if leftDelta == rightDelta: return min(left, right)
    if leftDelta < rightDelta: return left
    else: return right

arr = [60864,25176,27249,21296,20204]
target = 56803

# arr = [4,9,3]
# target = 10

# arr = [2,3,5]
# target = 10
print(findBestValue(arr, target))