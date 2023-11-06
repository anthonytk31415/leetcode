from math import sqrt
# iterate up to sqrt(k)
from collections import deque


def kthFactor(n, k):
    mid = sqrt(n)
    factors = deque()
    if int(mid) == mid: 
        factors.append(int(mid))
        start = int(mid)-1
    else: 
        start = int(mid)
    for i in range(start, 0, -1):
        if n % i == 0: 
            factors.appendleft(i)
            factors.append(int(n/i))
    factors = list(factors)
    print(factors)
    if 0 <= k-1 < len(factors):
        return factors[k-1]
    else: 
        return -1
    
n = 12
k = 3
print(kthFactor(n, k))

# n, k= 4, 4
# print(kthFactor(n, k))


     4, 2, 3, 1, 4, 1, 2
     1, 0, 1, 0, 1, 0, 1
max  4  4  4  4  8 
cmx  4  0  3  3  