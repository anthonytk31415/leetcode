from collections import Counter, deque

def findLeastNumOfUniqueInts(arr, k):
    counter = Counter(arr)
    numCountArr = []
    for x in counter.keys(): 
        numCountArr.append([counter[x], x])
    numCountArr.sort(key = lambda x: x[0])
    numCountArr = deque(numCountArr)
    while k > 0:
        curCount, curElement = numCountArr.popleft()
        if k >= curCount: 
            k -= curCount 
        else:
            curCount = curCount - k
            numCountArr.appendleft([curCount, curElement])
            k = 0
    return len(numCountArr)


arr = [4,3,1,1,3,3,2]
k = 3

arr = [5,5,4]
k = 1

print(findLeastNumOfUniqueInts(arr, k))