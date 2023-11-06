# https://docs.python.org/3/library/heapq.html#heapq.heapify

import heapq

arr = [30, 20, 1,4,2,6,8,10,3,7]

print(arr)
## min heapify on array in O(n) time
# heapq.heapify(arr)

# "delete" the min value in heap and return the value
# z = heapq.heappop(arr)

## max heapify on array in O(n) time 
# heapq._heapify_max(arr)

# print(arr)
# print(z)

### using python heaps
# def findKthLargest(nums, k):
#     import heapq
#     heapq._heapify_max(nums)
#     print(nums)
#     for _ in range(k):
#         z = heapq._heappop_max(nums)
#     return z

## using python heaps klargest; kind of like cheating 
# def findKthLargest(nums, k):
#     from heapq import nlargest 
#     return nlargest(k, nums)[-1]

## using sorted function
def findKthLargest(nums, k):
    return sorted(nums)[-k]



print(findKthLargest(arr, 4))