# there is an n such that b is a substring of n*a
# in order for this to happen, 
# a has to contain the prefix of b, a has to contain the suffix of b

# Time O(m*n), Space O(1) solution

# you can also implement a prefix-sum based one too that takes linear space and time. 
from math import inf 

def repeatedStringMatch(a, b):
    def determineCycle(i):
        cycles = 1
        for j in range(len(b)):
            if a[i] == b[j]:
                i += 1
                if i >= len(a) and j < len(b)-1: 
                    cycles += 1 
                    i = 0
            else: 
                return -1
        return cycles


    overallMin = inf
    for i in range(len(a)):
        if a[i] == b[0]:
            curRes = determineCycle(i)
            if curRes != -1: overallMin = min(overallMin, curRes)

    if overallMin == inf: return -1
    return overallMin

# a = "abcd"
# b = "cdabcdab"
# a = "a"
# b = "aa"
a = "abbab"
b = "bababbababb"

print(repeatedStringMatch(a, b))