# t = 8
# # sort the candidates
# [10,1,2,7,6,1,5]
# # >> sort

# [1,1,2,5,6,7,10]

# i = 0
# i = 0 + 1
# target = 8 - 1
# path = 1





# 1,1,1


# []
# []


# # >> trash #'s > target
# 1,1,2,5,6,7

# 1 -->  tSum = 1; tSum < target; --> add another one; bitmask = 1
# 1,1 -->  tSum = 2; tSum < target; --> add another one; bitmask = 11
# 1,1,2 --> tsum = 4; tSum < target; --> add another one; bitmask = 111
# 1,1,2,5 --> tSum = 9; tSum > target; --> backtrack to prev entered one; (after backtrack) bitmask = 110
# 1,1,5 --> tSum =7; tSum < target --> add another one; bitmask = 1101
# 1,1,5,6 --> tSum = 13; tSum > target --> backtrack to prev; bitmask = 1


# 1,2 -> tSum = 3; tSum < target --> add another one; bitmask = 101
# 1,2,5 --> tSum = 8 = target --> add result; backtrack; bitmask to add = 1011; backtrack 


# 1,1,1,1 > fail 
# 1,1,0,1,1 > fail 
# 1,1,0,0,1 > true
# 1,0,1,1 > true
# 0,1,1,1 > true but dupe
# 0,0,1,1,1 > false
# 0,0,1,0,1 > true
# 0,0,0,1,1 > false
# 0,0,0,0,1,1 > false

# - first, sort the array 
# - start with first element; 
#   - keep a running sum;
#   - Assign a bit mask to the sorted array:  
#

# - if the sum = target: 
# - if the sum < target, prepare to next loop
# - if the sum > 


# start with taking the first element and then do sort of backtracking
# take next element
# each element you take: if target - sum(elements) > 0: keep going
# if you add an element and that element equals the target sum: youre done, and backtrack (each subsequent item will increase sum)
# you always start with left most then go right, you never have to go "back" since we are doing combinations; you already considered the "back" guys

# now how do you program backtracking

# take 1: 
# t = 7

def combinationSum2(candidates, target): 
    ret = []
    dfs(sorted(candidates), target, 0, [], ret)
    return ret


# def dfs(nums, target, idx, path, ret):
#     # print(f'target = {target}, index = {idx}, path = {path}')
#     if target <= 0: 
#         if target == 0: 
#             print(f'path = {path}, index = {idx}')
#             ret.append(path)
#         return 
#     for i in range(idx, len(nums)):
#         print(f'index = {idx}, i = {i}, target = {target}, path={path}')
#         if i > idx and nums[i] == nums[i-1]:                                          # <--- this line allows you to prevent duplicates but logic is nuanced
#             print(f'nums[i] == nums[i -1]: {nums[i]}, {nums[i-1]}; index = {idx}, i = {i}, path = {path}')
#             continue
#         dfs(nums, target - nums[i], i+1, path + [nums[i]], ret)


# what is the time complexity? 

def dfs(nums, target, idx, path, ret):
    if target <= 0: 
        if target == 0:
            if path not in ret:  
                ret.append(path)
        return 
    for i in range(idx, len(nums)):
        dfs(nums, target - nums[i], i + 1, path + [nums[i]], ret)




# print(combinationSum2([1,1,2,5,6,7,10], 8))
print(combinationSum2([1,1,2], 2))