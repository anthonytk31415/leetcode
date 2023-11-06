from math import inf
def jump(nums):
    nums[-1] = 0
    for i in range(len(nums)-2, -1, -1):
        if nums[i] ==0:
            nums[i] = inf
        else: 
            nums[i] = 1 + min(nums[i+1:i + nums[i]+1])
        # print(nums, i)
    return nums[0]

nums = [2,3,1,1,4]
# 4: 2,3,1,1,0 
# 3: 2,3,1,1,0
# 2: 1,2,

# nums = [2,3,0,1,4]
print(jump(nums))