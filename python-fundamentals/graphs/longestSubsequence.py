from collections import deque, defaultdict


def longestSubsequence(arr, difference):
    lookup = defaultdict(deque)
    for i, x in enumerate(arr):
        lookup[x].append(i)

    print(lookup)

    visited = [False for _ in arr]
    
    for i in range()

  #   [0,1,2,3,4,5,6,7,8]
arr = [1,5,7,8,5,3,4,2,1]
difference = -2


print(longestSubsequence(arr, difference))

# 1, [0,8]
# 5, [1,4]
# 7, [2]
# 8, [3]
# 3, [5,]
# 4, [6]
# 2, [7]



# # you always want to choose the earliest index
# # if you discard an index, do you ever want it again? 
# x   x   x   x   x
# 1,5,2,6,3,7,4,8,5
#   y   y   y   y