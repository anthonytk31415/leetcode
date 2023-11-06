#find pivot index

def pivotIndex(nums):
    left = 0
    right = sum(nums) - nums[0]
    # if sum(nums)==0:
    #     return 0
    if len(nums) == 1:
        return 0
    if left == right:
        return 0
    for i in range(1,len(nums)):
        left = left + nums[i-1] 
        right = right - nums[i]
        if left == right:
            return i
    return -1

# nums = [2,1,-1]
nums = [1,7,3,6,5,6]
print(pivotIndex(nums))