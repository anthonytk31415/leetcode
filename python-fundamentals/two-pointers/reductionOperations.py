def reductionOperations(nums):
    j = len(nums) - 1
    res = 0
    nums.sort()
    while j > 0: 
        if nums[j] > nums[j-1]:
            res += len(nums)-1 - j + 1
        j -= 1

    return res