# https://leetcode.com/problems/rearrange-array-elements-by-sign/


# nums = even

def rearrangeArray(nums):
    pos = [x for x in nums if x >= 0]
    neg = [x for x in nums if x < 0]
    # print(pos,neg)
    for i in range(0, len(pos)):
        nums[2*i] = pos[i]
        nums[2*i + 1] = neg[i]
    return nums

from collections import deque

def rearrangeArray(nums):
    pos_q = deque()
    neg_q = deque()
    # print(pos,neg)
    res = []
    for i in range(0, len(nums)):
        x = nums[i]
        # add positive
        if x > 0: 
            pos_q.append(x)
        else: 
            neg_q.append(x)
        
    return res



nums = [3,1,-2,-5,2,-4]

rearrangeArray(nums)
print(nums)