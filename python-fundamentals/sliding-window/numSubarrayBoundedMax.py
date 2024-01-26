from math import inf

# sliding window
# trick: write out the candidates, and figure out how the permutations on teh sliding window are built

def numSubarrayBoundedMax(nums, left, right):
    res = 0
    leftIdx = 0
    curMax = -inf
    prevAdd = 0
    for rightIdx, rightVal in enumerate(nums):
        curMax = max(curMax, rightVal)
        if rightVal > right: 
            curMax = -inf 
            leftIdx = rightIdx + 1
            prevAdd = 0
        elif left <= curMax <= right: 
            if left <= rightVal <= right: 
                res += rightIdx - leftIdx + 1
                prevAdd = rightIdx - leftIdx + 1
            elif rightVal < left:  
                res += prevAdd

    return res


# nums = [2,9,2,5,6]
# left = 2
# right = 8


# nums = [2,1,4,3]
# left = 2
# right = 3

nums = [2,1,3,3,1, 1,4,1,2]

left = 2
right = 3


# 2, --> 1 (length)
# 21 --> 1 (prev)
# 3, 13, 213 --> 3 (length)
# 3, 33, 133, 2133 --> 4 (length)
# 31, 331, 1331, 21331 --> 4 (prev)
# 311, 3311, 13311, 213311 --> 4 (prev)
# 
# 2, 12 --> 2 (length)
# ans = 19

print(numSubarrayBoundedMax(nums, left, right))

# 2 --> 1; prevAdd = 1
# curMax = inf; leftIdx = 2; prevAdd = 0
# 2 --> 1: prevAdd = 1; leftIdx = 2; 
# 5, 25 --> 2; prevAdd = 2; leftIdx = 2
# 6, 56, 256 --> 3; prevAdd = 3; leftIdx = 3



# left, mid, right
# between mid and right,  
# right is the last number that is  

# nums = [2,1,3,3,1, 1, 4,1,2]

# 2, 21, 213, 2133
# 133, 13, 
# 33
# 3
# 3 

# 2 --> 1 (length; num in range)
# 21 --> 1 (last; num is < range)
# 3, 13, 213 --> 3 (length: num in range)
# 3, 33, 133, 2133 --> 4 (length between )
# 31, 331, 1331, 21331 --> 4 (last; num < range)
# 4 --> 0 
# 1 --> 0 (num < range)
# 2, 12 (lenght; num in range)


# left = 2
# right = 3


# nums = [2,1,4,3]
# left = 2
# right = 3

# 2, 21
# 3 



# nums = [2,9,2,5,6], left = 2, right = 8
# 2
# 2, 25, 256
# 5, 56, 
# 26

# find the smallest window that is valid. 
# then 