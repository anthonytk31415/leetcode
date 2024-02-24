
# def find132pattern(nums):


# (5, 10)(2, 4), 
# 5, 10, 2, 4, 0, 5
# # if bisecting gives you the last element and your num is > the endpoint, then pop and replace

# # after every iteration, if your current min and max is a wider interval than the one on top, pop it
# ## e.g. 2,4; then 0, 5
# 5, 10, 1, 3, 0, 1

    # stack = []
    # curMin = nums[0]
    # curMax = nums[0]
    # stack.append((curMin, curMax))
    # for i in range(1, len(nums)):
    #     curNum = nums[i] 

    #     idx = bisect_left(stack, curNum, key = lambda a, b: b - a)
    #     u, v = stack[idx]
    #     if u < curNum < v: return True
    #     if idx == len(stack) - 1:
    #         if curNum > v: 
    #             stack.pop()
    #             stack.append((u, curNum))
    #         elif curNum < u: 
    #             stack.append((curNum, curNum))

    #     # if idx == len(stack) then 

    #     return 

# def find132pattern(nums):
#     stack = []
#     for num in nums: 
#         popped = False
#         while stack and stack[-1] > num: 
#             popped = True
#             stack.pop()
        
#         if stack and popped: return True
#         stack.append(num)
#     return False


# every time you pop, you keep track of the largest popped number

# 11, 9,10,7,6,8,9


# print(find132pattern(nums))
from math import inf

def find132pattern(nums):
    stack = []
    maxPopped = -inf
    for i in range(len(nums)-1, -1, -1):
        num = nums[i]

        if stack and num < stack[-1] and num < maxPopped: return True
        while stack and num > stack[-1]: 
            maxPopped = max(maxPopped, stack.pop())
        stack.append(num)


    return False

# nums = [-1,3,2,0]
nums = [3,5,0,3,4]
# nums = [1,2,3,4]

nums = [ 3,11, 9,10,7,6,8,9]

print(find132pattern(nums))
