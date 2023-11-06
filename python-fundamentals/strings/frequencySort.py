# 528

from heapq import heappop, heappush

# time: o(n log n)
# space: O(n)

def frequencySort(s):
    counter = {}
    for char in s: 
        if char not in counter: 
            counter[char] =1
        else: 
            counter[char] +=1
    
    heap = []
    for char in counter: 
        heappush(heap, (-counter[char], char))

    res = ''
    # now assemble based on max elements
    while heap:
        # print(res) 
        z = heappop(heap)
        n, c = z
        res = res + c*(-n)
    return res

print(frequencySort('abracadabra'))