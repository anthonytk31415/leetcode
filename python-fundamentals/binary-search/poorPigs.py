from math import ceil, floor

def factorial(n):
    res = 1
    for i in range(1, n+1, 1):
        res *= i
    return res

def nChooseK(n, k):
    return factorial(n)/(factorial(k)*factorial(n-k))

def sumNChooseK(n):
    res = 0
    for i in range(1, n+1, 1):
        res += nChooseK(n, i)
    return res


# 46 minTest
# 15 mnDie
# ==> 3 cycles (floor(46/15))

# 100 buckets
# 3 cycles
# ==> 34 buckets (ceil(100/3))


def poorPigs(buckets, minutesToDie, minutesToTest): 
    numCycles = floor(minutesToTest/minutesToDie)

    bucketCoverage = ceil(buckets/numCycles)

    if numCycles == 1: 
        bucketCoverage -= 1

    left = 1
    right = bucketCoverage
    
    # sumNChooseK: 
    while left <= right: 
        mid = (left + right) // 2
        pigsCoverage = sumNChooseK(mid)
        if pigsCoverage == bucketCoverage: 
            return mid
        if pigsCoverage < bucketCoverage: 
            left = mid + 1
        else: 
            right = mid - 1


    return left 

# print(ceil(10/3))

# buckets = 4
# minutesToDie = 15
# minutesToTest = 15


# buckets = 4
# minutesToDie = 15
# minutesToTest = 30
# print(poorPigs(buckets, minutesToDie, minutesToTest))



buckets = 1000
minutesToDie = 15
minutesToTest = 60

# print(poorPigs(buckets, minutesToDie, minutesToTest))


# print(nChooseK(5,5))
# 252+210+120+45+10 = 637

# 5 + 10 + 10 + 5 + 1 = 31

# need coverage of 250
print(sumNChooseK(3))