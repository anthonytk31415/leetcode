from collections import Counter
from math import inf

def minDominoRotations(tops, bottoms):
    countTops = Counter(tops)
    countBottoms = Counter(bottoms)
    countSame = Counter()
    for i in range(len(tops)):
        if tops[i] == bottoms[i]:
            countSame[tops[i]] += 1
            countTops[tops[i]] -= 1
            countBottoms[tops[i]] -=1

    overallMax = inf
    for i in range(1, 7):
        if countTops.get(i,0) + countBottoms.get(i, 0) == len(tops) - countSame[i]: 
            overallMax = min(overallMax, min(countTops.get(i, 0), countBottoms.get(i, 0)))

    if overallMax == inf: return -1
    return overallMax


# tops =    [2,1,2,4,2,2]
# bottoms = [5,2,6,2,3,2]

# tops =    [2,3,2,1,1,1,2,2]
# bottoms = [2,1,2,1,1,3,1,1]

tops =    [3,5,1,2,3]
bottoms = [3,6,3,3,4]
print(minDominoRotations(tops, bottoms))
