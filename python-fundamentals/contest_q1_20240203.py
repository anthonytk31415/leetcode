def returnToBoundaryCount(nums):
    curSum = 0
    res = 0
    for num in nums: 
        curSum += num
        if curSum == 0: res += 1

    return res 

nums = [2,3,-5]
nums = [3,2,-3,-4]
print(returnToBoundaryCount(nums))