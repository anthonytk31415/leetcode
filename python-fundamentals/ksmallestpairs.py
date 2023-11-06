from heapq import heappush, heappop


# this is O(m * n); too slow
def kSmallestPairs(nums1, nums2, k):
    minHeap = []
    for x in nums1: 
        for y in nums2: 
            heappush(minHeap, (x + y, (x, y)))

    res = []
    for _ in range(k):
        if minHeap: 
            curSum, coords = heappop(minHeap)
            res.append(coords)
        else: 
            break
    return res

# this is O(k*logk) Time; 
# Space; O(k)

def kSmallestPairs(nums1, nums2, k):
    m, n = len(nums1), len(nums2)
    minHeap =[(nums1[0] + nums2[0], (0, 0))]
    e = 0
    res = []
    visited = set()
    visited.add((0,0))
    while e < k: 
        if minHeap: 
            curSum, coords = heappop(minHeap)
            i,j = coords
            res.append((nums1[i],nums2[j]))
            e +=1
            for u, v in [(i+1, j), (i, j+1)]:
                if (u,v) not in visited and 0 <= u < m and 0 <= v < n:
                    visited.add((u,v))
                    heappush(minHeap, (nums1[u] + nums2[v], (u, v)))
        else: 
            break
    return res


nums1 = [1,1,2]
nums2 = [1,2,3]
k = 10
# nums1 = [1,7,11] 
# nums2 = [2,4,6]
# k = 3

print(kSmallestPairs(nums1, nums2, k))