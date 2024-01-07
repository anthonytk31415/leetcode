from collections import Counter
from heapq import heappush, heappop
def maximumSetSize(nums1, nums2):

    a, b = Counter(nums1), Counter(nums2)
    limA, limB = len(nums1)/2, len(nums2)/2
    commonA, commonB, distinctA, distinctB = [], [], [], []

    for x in [z for z in a.keys()]: 
        if x in b: 
            heappush(commonA, [a[x], b[x], x])
            del a[x]
            del b[x]
        else: 
            heappush(distinctA, [-a[x], x])
            del a[x]

    for x in [z for z in b.keys()]: 
        heappush(distinctB, [-b[x], x])
        del b[x]
        
    # print(a, b, commons, distinctA, distinctB)
    # remove ones that are common; do with the smallest

    print(distinctA, distinctB, commonA, commonB)

    while commonA and (limA > 0):
        aCount, bCount, x = heappop(commonA)
        if aCount <= limA: 
            limA -= aCount
            heappush(distinctB, [-bCount, x])
        else: 
            heappush(commonB, [bCount, aCount - limA, x])
            limA = 0

    while commonA: 
        aCount, bCount, x = heappop(commonA)
        heappush(commonB, [bCount, aCount, x])

    while commonB and (limB > 0):
        bCount, aCount, x = heappop(commonB)
        if bCount <= limB: 
            limB -= bCount
            heappush(distinctA, [-aCount, x])
        else: 
            heappush(commonB, [bCount-limB, aCount, x])
            limB = 0

    # print("distincts A: {}, B: {}, limA {}, limB {}".format( distinctA, distinctB, limA, limB))

    while limA > 0: 
        aCount, x = heappop(distinctA)
        aCount = -aCount
        if aCount > 1:
            if aCount-1 <= limA:
                heappush(distinctA, [-1, x])
                limA -= aCount-1
            else: 
                heappush(distinctA, [-(aCount - limA), x])
                limA = 0
        else: 
            limA -= 1
    # print("distincts A: {}, B: {}, limA {}, limB {}".format( distinctA, distinctB, limA, limB))

    while limB > 0: 
        bCount, x = heappop(distinctB)
        bCount = -bCount
        if bCount > 1:
            if bCount-1 <= limB:
                heappush(distinctB, [-1, x])
                limB -= bCount-1
            else: 
                heappush(distinctB, [-(bCount - limB), x])
                limB = 0
        else: 
            limB -= 1

    # print(distinctA, distinctB, commonA, commonB)
    #return all 3 length of commonB and the two distincts A and B
    return len(distinctA) + len(distinctB) + len(commonB)



nums1 = [1,2,3,4,5,6]
nums2 = [2,3,2,3,2,3]


nums1 = [1,1,2,2,3,3]
nums2 = [4,4,5,5,6,6]


nums1 = [1,2,1,1]
nums2 = [1,2,3,4]

print("res: ", maximumSetSize(nums1, nums2))



# a = Counter(nums1)
# for x in a: 
#     print(a[x], x)