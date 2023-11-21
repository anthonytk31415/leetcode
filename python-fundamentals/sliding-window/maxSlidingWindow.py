# 0, 1, 2, 3, 4
# k = 2
## evict when i ==
# 


# we're going to use monotonic queue 
# invariant of queue: the top of the queue will always be the largest element
# - we'll use a sliding window
from collections import deque 
def maxSlidingWindow(nums, k):

    res = []
    queue = deque()
    for i, num in enumerate(nums):
        # remove from the back of the queue all elements < num; that way the queue is always decreasing, with the largest element in the front
        # that way; anything in the queue will be > num; for the remainder of the time num is in the queue, num will be the smallest element
        while queue and nums[queue[-1]] < num: 
            queue.pop()

        # now append num to queue 
        queue.append(i)

        # remove from the front of the queue if the window is out of range
        if queue[0] <= i - k: 
            queue.popleft()

        print(queue, i, num)
        # append to the res the item on the back of the deque, i.e. the max
        if i >= k-1:
            res.append(nums[queue[0]])
    return res

nums = [1,3,-1,-3,5,3,6,7]
k = 3

print("answer: ", maxSlidingWindow(nums, k))