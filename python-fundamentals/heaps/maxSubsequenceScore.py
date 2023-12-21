from math import inf 
from collections import deque 
from bisect import insort

from heapq import heappush, heappop

#  new one is n log n; old one was n^2 for the insort command

# Intuition: your k choices are driven by y* in nums2. Once you have y, you can pick 3 largest 
# elements where its corresponding y is >= to the y*. 
# So create a zipped nums1/nums2. sort by nums2 portion in descending order. 
# Then iterate x,y = num across nums. Keep a window-minheap. insert each x and heap-pop if length > k. 
# Keep track of the sum of the window. Multiply sum by y. 

# Time: O(nlogn) for sorting and inserting to the heap. 
# Space: O(n) for the window. 


# Previously, I was using a window with doing insort. that was good enough speed for the concert. 

def maxScore(nums1, nums2, k):
    nums = [[x, y] for x, y in zip(nums1, nums2)]
    nums.sort(key = lambda x: -x[1])
    window = []
    curSum = 0
    maxScore = -inf
    for x, y in nums:
        heappush(window, x)
        curSum += x
        if len(window) > k: 
            curSum -= heappop(window)
        if len(window) == k: 
            maxScore = max(maxScore, curSum*y)
    return maxScore

# nums1 = [1,3,3,2]
# nums2 = [2,1,3,4]
# k = 3

nums1 = [4,2,3,1,1]
nums2 = [7,5,10,9,6]
k = 1


print(maxScore(nums1, nums2, k))

# d = deque([1,2,3])
# print(d, sum(d))

# how to maintain an array of length 3 that is sorted and can insert and evict elements
# d = deque [a, b, c]
# if cur >= c: 
#     d.append(cur)
#     d.popleft()
# elif cur <= a: # dont do anything
# else: 
#     maybePutBack = cur.popleft()
#     if cur > b:
#         # pop b, append left cur, append left b
#     else: 
#         # append cur




# n1=[2,3,1,3]
# n1=[2,5,6,8]
# n2=[4,3,2,1]


# 8,15,12,8



# if you have a n2, you take all other n2's that are higher. 