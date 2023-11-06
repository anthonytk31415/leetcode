def firstMissingPositive(nums):
    

    for i in range(len(nums)): 
        prev = None
        while nums[i] != i + 1  and 1 <= nums[i] < len(nums) + 1: 
            curNum = nums[i]
            if prev == curNum: 
                break
            prev = curNum
            nums[i], nums[curNum - 1] = nums[curNum - 1], nums[i]

    for j in range(len(nums)):
        if j + 1 != nums[j]: 
            return j + 1
    return len(nums) + 1


# nums = [3,4,-1,1]
# nums = [7,8,9,11,12]
nums = [1,2,0] 
# nums = [1]
# nums = [1,2, 3, 7]
# nums = [1,1]
print(firstMissingPositive(nums))