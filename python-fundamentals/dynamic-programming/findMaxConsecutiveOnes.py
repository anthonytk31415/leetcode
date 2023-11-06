def findMaxConsecutiveOnes(nums):

    global_max = 0
    cur_max = 0
    if nums[0] == 1: cur_max = 1
    if len(nums) == 1:
        return max(cur_max, global_max)    
    for i in range(1, len(nums)):
        if nums[i] == 1:
            cur_max +=1
            global_max = max(cur_max, global_max)
        elif nums[i] == 0: 
            cur_max = 0
    return global_max

# nums = [1,1,0,1,1,1]
nums = [1,0,1,1,0,1]
print(findMaxConsecutiveOnes(nums))

