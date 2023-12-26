# n dice, k faces numbered 1 to k, target 


# dynamic programming: 
# Time: O(n^2)
# Space: O(n*target)

from functools import lru_cache
def numRollsToTarget1(n, k, target):    
    @lru_cache(None)
    def helper(n, w):
        res = 0
        if w < n or w > n*k: res = 0
        elif n == 1: res = 1        
        else: 
            for i in range(1, k+1):
                if w - i > 0: res += helper(n-1, w - i)
        return res

    for i in range(1, n, 1):
        for j in range(1, min(k*i, target) + 1, 1): 
            helper(i, j)

    return helper(n, target) % (10**9 + 7)

def numRollsToTarget(n, k, target):
    memo = {} ## num ways to get w = target with n dice

    def helper(n, w):
        if (n,w) in memo: return memo[(n,w)]
        res = 0
        if w < n or w > n*k: res = 0
        elif n == 1: res = 1        
        else: 
            for i in range(1, k+1):
                if w - i > 0: res += helper(n-1, w - i)
        memo[(n, w)] = res
        return res

    for i in range(1, n, 1):
        for j in range(1, min(k*i, target) + 1, 1): 
            helper(i, j)

    return helper(n, target) % (10**9 + 7)



# n = 2
# k = 6
# target = 7
# n = 1
# k = 6
# target = 3

n = 30
k = 30
target = 500

# n = 1
# k = 2
# target = 3

print(numRollsToTarget( n, k, target))