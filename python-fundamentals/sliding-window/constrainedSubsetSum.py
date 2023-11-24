from collections import deque

def constrainedSubsetSum(nums, k):

    # the queue will store (sum, idx)
    # invariant 1: queue[0] is always the largest sum within the window 
    queue = deque()
    curMax = max(nums)

    for i, num in enumerate(nums):
        curSum = num
        # if largest is > 0, pick it up; else don't
        if queue: 
            curSum = max(num + queue[0][0], num)  
        while queue and queue[-1][0] < curSum: 
            queue.pop()

        curMax = max(curMax, curSum)
        queue.append((curSum, i))

        if queue[0][1] == i - k: 
            queue.popleft()

    return max(queue[-1][0], curMax)

nums = [10,-2,-10,-5,20]
k = 2
# nums = [-1, 1,2,3,-5,-6,-7, 1, 4, 1, 12, 19, -4, 3, 2]
# k = 2

# nums = [-1,-2,-3]
# k = 1
print(constrainedSubsetSum(nums, k))


# print(sum([1, 4, 1, 12, 19, 3, 2]))

from heapq import heappush, heappop

heappush(arr, (1,2))
heappop(arr)