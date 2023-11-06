# Time(O(nlogn))
# space O(n)

# count the elements, see if x and 2x in the set or x and x/2. 
# you have a tricky edge case with 0: you need pairs of 0's for success.

from collections import Counter
def canReorderDoubled(arr):
    counter = Counter(arr)
    countNums = len(arr)
    for x in arr:
        if x in counter and counter[x] >0:
            if 2*x in counter and counter[2*x] > 0: 
                counter[x] -=1
                counter[2*x] -=1
                countNums -=2
            elif x %2 == 0 and int(x/2) in counter and counter[int(x/2)] > 0:
                counter[x] -=1
                counter[int(x/2)] -=1
                countNums -=2
    print(countNums, (counter))
    return countNums==0

arr = [2,4,0,0,8,1]
print(canReorderDoubled(arr))