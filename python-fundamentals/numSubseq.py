# once you find an i and j that satisfies min + max <= target, 
# then all subsequences that contain i will also be a candidate
# (including i itself and alone)

# then increase i +=1 and see if that is ok

# 1,2,3,4; n = 4
# 1: 1
# 2: 3; n-1
# 3: 2; n-2
# 4: 1; n-3


# 1,2; n = 2
# 1: 1
# 2: n-1 = 1

# 1,2,3; n = 3
# 1: 1
# 2: n-1 = 2
# 3: n-2 = 1


# 1,2,3,4,5
# 1:
# 2:
# 3:
# 4:
# 5:

# 2,3,3,4,6,7
# 
# 1: 1, 
# 2: 5, 
# 3: 

from functools import lru_cache
from itertools import combinations, permutations 

# print(list(combinations([0,1,2,3], 2)))
# print(list(permutations([0,1,2,3], 2)))

@lru_cache(None)
def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

def nChooseK(n, k):
    return (factorial(n)/(factorial(k)*factorial(n - k)))

def numSubseq(nums, target):
    nums.sort()
    i = 0
    j = len(nums) - 1
    counter = 0

    @lru_cache(None)
    def perms(length):
        res = 1
        for i in range(1, length):
            # res += len(list(combinations(range(length-1), i)))
            res += nChooseK(length - 1, i)
        return res

    while i <= j: 
        delta = nums[i] + nums[j]
        if delta <= target: 
            length = j - i + 1
            counter += perms(length)
            i +=1
        else: 
            j -=1

    return counter
    # return counter % (10**9 + 7) 

# nums = [3,5,6,7]
# target = 9

# nums = [3,3,6,8]
# target = 10
# nums = [2,3,3,4,6,7]
# target = 12

nums = [27,21,14,2,15,1,19,8,12,24,21,8,12,10,11,30,15,18,28,14,26,9,2,24,23,11,7,12,9,17,30,9,28,2,14,22,19,19,27,6,15,12,29,2,30,11,20,30,21,20,2,22,6,14,13,19,21,10,18,30,2,20,28,22]
target = 31

# 688052206

print(numSubseq(nums, target))

