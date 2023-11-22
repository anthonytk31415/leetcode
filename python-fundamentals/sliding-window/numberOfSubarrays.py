

from itertools import groupby


def numberOfSubarrays(nums, k):
    arr = []
    evenStreak = 0
    for i, num in enumerate(nums):
        if num % 2 == 0: 
            evenStreak += 1
        else: 
            if evenStreak > 0: 
                arr.append((0, evenStreak))
                evenStreak = 0
            arr.append((1,1))
    if evenStreak > 0: 
        arr.append((0, evenStreak))
        evenStreak = 0

    res = 0
    kCounter = 0
    left = 0
    for right, curTuple in enumerate(arr):
        val, freq = curTuple
        if val == 1: 
            kCounter += 1

        if kCounter == k: 
            while left < len(arr) and arr[left][0] == 0: 
                left += 1
            leftLength, rightLength = 1,1 
            if left - 1 >= 0 and arr[left - 1][0] == 0: 
                leftLength = arr[left-1][1] + 1
            if right + 1 < len(arr) and arr[right + 1][0] == 0: 
                rightLength = arr[right + 1][1] + 1
            res += leftLength * rightLength
            kCounter -= 1
            left += 1
    return res        


# 

from collections import defaultdict

def numberOfSubarrays1(nums, k):
    countOdds = 0
    prefix = defaultdict(int)
    prefix[countOdds] +=1
    for i in range(len(nums)):
        if nums[i] % 2 == 1: 
            countOdds +=1
        prefix[countOdds] +=1

    res = 0
    print(prefix)
    for c in prefix:
        if c - k in prefix:
            res += prefix[c] * prefix[c - k]
    return res


# s = "222122212211"
# s = "2221222122"
# nums = [int(x) for x in s]
nums = [2,2,2,1,2,2,1,2,2,2]
k = 2

arr = [1,2,3,4,5]
prefixSum = [x for x in arr]
for i in range(1, len(prefixSum)):
    prefixSum[i] = prefixSum[i] + prefixSum[i - 1]
    
print("Prefix Sum: ", prefixSum)
i, j = 2, 4
print("sum from i : {} to j: {} = prefixSum[{}] - prefixSum[{}] = {}".format(i, j, j, i + 1, prefixSum[j] - prefixSum[i]))
# finding the sum from i + 1 to j means taking prefixSum[j] - prefixSum[i]

print(nums)

print(numberOfSubarrays1(nums, k))