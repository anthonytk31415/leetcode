# https://leetcode.com/problems/koko-eating-bananas/description/

# time: n log n
# space: o(n)

from math import ceil

def minEatingSpeed(piles, h):
    left = 1
    right = max(piles)
    if h == len(piles):
        return max(piles)
    
    while left < right:             #notice we dont take left == right; if that's the case then we can just return right and we found answer
        mid = (left + right) // 2
        hours_needed = sum([ceil(x/mid) for x in piles])

        if hours_needed <= h:       # if are within hours, see if you can get to smaller h; right will always be an acceptable answer
            right = mid 
        elif hours_needed > h: 
            left = mid + 1          # take the one just above left; remember that right give you the answer
    return right



piles = [1,1,1,999999999]
h = 10

# piles = [312884470]
# h = 312884469
print(minEatingSpeed(piles, h))