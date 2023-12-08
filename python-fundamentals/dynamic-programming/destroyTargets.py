# mods = [ num modulo space] = [min integer, total numbers]
# Kind of dynamic programming since it takes advantage of a prior 
# result. Key use of modulo. 

from collections import defaultdict
from math import inf

def destroyTargets(nums, space):
    mods, maxDestroy, minValue= {}, 0, inf
    for num in nums:     
        modulo = num % space
        if modulo not in mods: 
            mods[modulo] = [num, 1]
        else: 
            mods[modulo] = [min(num, mods[modulo][0]), mods[modulo][1] + 1]

        if mods[modulo][1] > maxDestroy: 
            maxDestroy = mods[modulo][1]
            minValue = mods[modulo][0]
        elif mods[modulo][1] == maxDestroy: 
            maxDestroy = max(maxDestroy, mods[modulo][1])
            minValue = min(minValue, mods[modulo][0])

    return minValue

# OK Lee Solution; study this: 

def destroyTargetsLee(A, space):
    count = Counter(a % space for a in A)
    maxc = max(count.values())
    return min(a for a in A if count[a % space] == maxc)

# nums = [3,7,8,1,1,5]
# space = 2

# nums = [1,3,5,2,4,6]
# space = 2

nums = [1,5,3,2,2]
space = 10000

print(destroyTargets(nums, space))