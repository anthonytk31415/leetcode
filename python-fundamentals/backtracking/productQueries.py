
print(10**9 < 2**30)

def binarySearchLargestPowerTwo(n):
    left = 0
    right = 30
    while left + 1 < right: 
        mid = (left + right)//2
        if 2**mid == n: 
            return mid
        if 2**mid < n: 
            left = mid
        else: 
            right = mid
    return left 

def powers(n):
    if n == 1: 
        return [1]
    res = []
    curPower = binarySearchLargestPowerTwo(n)
    while n >0: 
        if n - 2**curPower >= 0: 
            n -= 2**curPower
            res.append(2**curPower)
        else: 
            curPower -= 1
    return res[::-1]
    # lets binary search the correct power to start with 

print(powers(15))




        


def productQueries(n, queries):

    def binarySearchLargestPowerTwo(n):
        left = 0
        right = 30
        while left + 1 < right: 
            mid = (left + right)//2
            if 2**mid == n: 
                return mid
            if 2**mid < n: 
                left = mid
            else: 
                right = mid
        return left 

    def powers(n):
        if n == 1: 
            return [1]
        res = []
        curPower = binarySearchLargestPowerTwo(n)
        while n >0: 
            if n - 2**curPower >= 0: 
                n -= 2**curPower
                res.append(2**curPower)
            else: 
                curPower -= 1
        return res[::-1]
        # lets binary search the correct power to start with 


    # build powers
    powers = powers(n)

    res = []
    # do the queries
    for start, end in queries: 
        cur = 1
        for j in range(start, end + 1):
            cur *= powers[j]
        res.append(cur % (10**9 + 7))
    return res


n = 15
queries = [[0,1],[2,2],[0,3]]

print(productQueries(n, queries))