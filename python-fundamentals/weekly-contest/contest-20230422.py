print('yo')


def findDelayedArrivalTime(arrivalTime, delayedTime):
    return (arrivalTime + delayedTime) % 24

# arrivalTime = 13
# delayedTime = 11


# arrivalTime = 15
# delayedTime = 5 
# print(findDelayedArrivalTime(arrivalTime, delayedTime))


def sumOfMultiples(n):
    nums = set()
    for i in [3,5,7]:
        for x in range(i, n + 1, i):
            nums.add(x)
    
    return sum(nums)

# print(sumOfMultiples(10))
# print(sumOfMultiples(9))

# TLE

from collections import deque
from bisect import bisect_left, insort


# arr = [0,1,2,3,4]

# print(bisect_left(arr, 1))

def getSubarrayBeauty(nums, k, x):

    i = k-1
    cur_k = sorted(nums[0:k-1])
    count_negs = 0
    for num in cur_k: 
        if num < 0:
            count_negs +=1

    res = []
    while i < len(nums):
        if nums[i] < 0:
            count_negs +=1
        idx = bisect_left(cur_k, nums[i])

        insort(cur_k, nums[i], idx)
        # cur_k = cur_k[:idx] + [nums[i]] + cur_k[idx:]
        
        # print(cur_k)
        # append the beauty of the subarray k
        if count_negs < x: 
            res.append(0)
        else: 
            res.append(cur_k[x-1])         # kth smallest so minus 1
        
        # take care of popped for cur_k and count_negs 
        popped = nums[i - k + 1]
        popped_idx = bisect_left(cur_k, popped)
        cur_k.pop(popped_idx)

        if popped < 0:
            count_negs -=1

        i += 1
    return res

# nums = [1,-1,-3,-2,3]
# k = 3 
# x = 2



# nums = [-1,-2,-3,-4,-5]
# k = 2
# x = 2

# nums = [-3,1,2,-3,0,-3]
# k = 2
# x = 1

# print(getSubarrayBeauty(nums, k, x))

def gcd(a, b):
    if b == 0: 
        return a
    else: 
        return gcd(b, a%b)

# print(gcd(3,4))
# print(gcd(6, 14))

from functools import lru_cache

def minOperations(nums):
    count_ones = 0
    count_gcd = 0

    for x in nums: 
        if x == 1: count_ones +=1
    if count_ones > 0 : 
        return len(nums) - count_ones

    @lru_cache(None)
    def helper(nums):
        print(nums)
        check = False
        for i in range(1, len(nums)):
            if nums[i] != nums[0]:
                check = True
                break
        if check == False: 
            return -1

        res = []
        for i in range(1, len(nums)):        
            print(nums[i], nums[i-1])
            cur_gcd = gcd(nums[i], nums[i-1])
            
            if cur_gcd == 1:
                return 1 + len(nums) - 1             
            else: 
                new_nums = tuple(list(nums[:i]) + [cur_gcd] + list(nums[i+1:]))
                res.append(1 + helper(new_nums))


        return min(res)
    # now do gcd on end points
        
    return helper(tuple(nums))


# def minOperations(nums):
    
# gcd(2,6)

# nums = [2,6,3,4]
# nums = [2,10,6,14]
nums = [6,10,15]
print(minOperations(nums))
# 
# print(gcd(10, 15))
# print(gcd(2,15))