from math import inf 
def numberOfArithmeticSlices(nums):
    res = 0
    delta = -inf
    length = 1
    for i in range(1, len(nums)):
        curDelta = nums[i] - nums[i-1]
        if curDelta == delta: 
            length += 1
        else: 
            if length >= 3:
                k = length - 2
                res += k*(k+1)//2
            length = 2
            delta = curDelta
    if length >= 3:
        k = length - 2
        res += k*(k+1)//2
    return res

nums = [1,2,3,4]
nums = [1,3,5,7,9]
print(numberOfArithmeticSlices(nums))