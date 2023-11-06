from heapq import heappush, heappop
from collections import Counter


# first, pop the heap, add that char, decrement the count of that char, then put that in "last"
# now proceed with the while loop 
# cur: pop the next element, then add that char and decrement the count of that char,
# then push the "last" to the heap if the count of the "last" is > 0; then the cur becomes the last


def reorganizeString(s):
    if len(s) <= 1:
        return s

    maxHeap = []
    letterCount = Counter(s)
    for x in letterCount:
        heappush(maxHeap, [-1*letterCount[x], x])

    res = []
    last = heappop(maxHeap)
    nLast, charLast = last
    res.append(charLast) 
    nLast += 1

    while maxHeap:
        cur = heappop(maxHeap)
        print(cur)
        nCur, charCur = cur
        res.append(charCur)
        nCur += 1

        if nLast < 0:
            heappush(maxHeap, [nLast, charLast])
        nLast, charLast = [nCur, charCur]

    if len(res) != len(s):
        return ""

    return ('').join(res)


print(reorganizeString("aaaabbbcccdddd"))
