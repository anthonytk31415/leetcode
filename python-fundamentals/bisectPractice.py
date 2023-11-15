from bisect import bisect, bisect_left 

arr = [1,2,4,4,7]

idx = bisect(arr, 4)
idx_left = bisect_left(arr, 4)
print(idx, idx_left)

arr1 = [[1,2], [4,19]]

idx = bisect(arr1, 7, key=lambda x: x[1])
print(idx)

from collections import Counter

arr = [1,1,1,1,2,2,2,2,3,3,3,3,3]
counts = Counter(arr)
print(counts)

print(counts.get(8, 2))

from collections import OrderedDict

myDict = OrderedDict()
myDict[1] = 2
myDict[3] = 4
myDict[5] = 7
myDict[8] = 9

print(myDict.popitem(last=False))
print(myDict.popitem())