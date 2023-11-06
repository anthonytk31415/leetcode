# threeSumClosest

## 9:44

# the trick is to use two pointers:
# - sort the nums array
# - i, j, k = 1st, 2nd, 3rd
# - We're only concerned with combinations (order does not matter). Thus
#   we can iterate i < j < k and i across 0 to len(nums) - 1 to get all combinations
# - We can even save more time: at each step of iterating j and k, we know if we need to get 
#   the sum bigger or smaller. increasing j index will make the sum larger; decreasing k will 
#   get the sum smaller. Thus:
#      - sum < target --> j +=1
# #    - sum > target --> k -=1

# Time: O(N^2) for i iterates over n, and while i, you iterate over other elements up to n times
# Space: O(1), ony pointers needed 

def threeSumClosest(nums, target):
    nums.sort()                                             # sort to set up dual pointers
    res = nums[0] + nums[1] + nums[2]                       # take a starting point
    for i in range(len(nums)):
        j , k = i + 1, len(nums) - 1                        # start with smallest, largest of pair,
        while j < k:
            temp_sum = nums[i] + nums[j] + nums[k]
            if target == temp_sum:                          # (1) sum equals target exit cond
                return temp_sum 
            if abs(target-temp_sum) < abs(target - res):    # (2) update res if it's better
                res = temp_sum
            if temp_sum < target:                           # (3) get larger temp_sum
                j +=1
            else:                                           # (4) get smaller temp_sum 
                k -=1   
    return res




a = [-4,-1,1,2]

x = threeSumClosest(a, 2)
print(x)

# Time: n^2 * log(n) 


# i= 1
# j = 3
# # a = [0, 1,2,3,4,5,6,7]
# a = [-4,-1,1,2]
# t = 1
# z = -4
# y = -1

# b = sorted(a, key=lambda x: abs(t - x - y - z))


# # b = a[:i] + a[i+1:j] + a[j+1:]
# print(b)




# is this too slow? 

# def threeSumClosest(nums, target):
#     from math import inf
#     nums = sorted(nums)
#     curTargetMin = inf
#     curSum = None
#     for i in range(len(nums)-2):
#         for j in range(i+1, len(nums)-1):
#             b = nums[j+1:]
#             x_star = sorted(b, key = lambda x: abs(target - nums[i] - nums[j] - x))[0]
#             temp_sum = nums[i] + nums[j] + x_star
#             # print(nums[i], nums[j], x_star, temp_sum)
#             if abs(target - temp_sum) < curTargetMin: 
#                 curTargetMin = abs(target - temp_sum)
#                 curSum = temp_sum
#     return curSum

# still too slow; 
# def threeSumClosest(nums, target):
#     from itertools import combinations
#     from math import inf
    
#     curTargetMin = inf
#     curSum = None
#     for x in list(combinations(nums, 3)):
#         temp_sum = sum(x)
#         if abs(target - temp_sum) < curTargetMin:
#             curTargetMin = abs(target - temp_sum)
#             curSum = temp_sum

#     return curSum
