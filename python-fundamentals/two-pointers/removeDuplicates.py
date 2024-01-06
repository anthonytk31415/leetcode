from math import inf
def removeDuplicates(nums):
    countChars = 1
    prevNum = -inf
    i = 0
    for j, jNum in enumerate(nums):
        if jNum != prevNum: 
            prevNum = jNum
            countChars = 0
        countChars += 1
        if countChars < 3: 
            nums[i], nums[j] = nums[j], nums[i]
            i += 1        
    return i

nums = [1,1,1,2,2,3]
print(removeDuplicates(nums))
print(nums)