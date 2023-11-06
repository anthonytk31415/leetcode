from collections import deque

def nextGreaterElement(nums1, nums2):
    lookup = {}
    for x in nums1:
        lookup[x] = -1
    
    q = deque()
    for i, n in enumerate(nums2):
        while q and nums2[q[-1]] < n:
            cur = q.pop()
            lookup[nums2[cur]] = n
        q.append(i)

    res = [-1] * (len(nums1))
    for i in range (len(nums1)):
        res[i]= lookup[nums1[i]] 
    print(lookup)
    return res

# Time: o(n)
# Space: o(n) for n elemenets of nums1
