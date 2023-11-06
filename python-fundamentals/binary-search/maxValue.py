#  https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/?envType=daily-question&envId=2023-10-18

# Approach:
# - binary search for the answer
# - use sum of n terms of an arithmetic sequence to get: sum of n terms = (s_start + s_end) * n / 2
# - realize that the "peak" at the index should be the max term
# - since each i of the array must be a positive number (some int > 0), you can do maxSum -= n and just build a staircase
#   of 1, 2, ... peak at index, peak - 1, ... 1 / and the rest will be 0's
 
# Time: O(n log n)
# Space: O(1)

def maxValue(n, index, maxSum):

    def sumN(start, end, n): 
        return n*(start + end)/2
    if n == 1: return maxSum
    maxSum -= n
    left = 0
    right = maxSum
    while left <= right: 
        mid = (left + right)//2
        curSum = 0
        curSum += mid
        # calculate curSum left side and right side: n/2(a + an); 

        # calc left: 
        leftLength = index
        end = mid - 1
        if leftLength <= mid - 1:  
            start = end - leftLength + 1
        else: 
            start = 1
        curSum += sumN(start, end, min(mid - 1, index))

        # calc rigth: 
        rightLength = n - 1 - index
        end = mid - 1
        if rightLength <= mid - 1: 
            start = end - rightLength + 1
        else: 
            start = 1
        curSum += sumN(start, end, min(mid - 1, rightLength))

        # print("curSum", curSum, "mid", mid, "maxsum: ", maxSum, "left", left, "right", right)
        if curSum == maxSum: 
            return mid + 1
        elif curSum > maxSum: 
            right = mid - 1
        else: 
            left = mid + 1 



    return right + 1


# maxSide = h-1


# pyramid - leftDelta - rightDelta
# n = 4
# index = 0
# maxSum = 4
# expected: 1

# n = 4
# index = 2
# maxSum = 6

# n = 6
# index = 1
# maxSum = 10


# n = 6
# index = 0
# maxSum = 27
# ans: 7

# 7 6 5 4 3 2

# 7 6 5 4 3 2

print(maxValue(n, index, maxSum))