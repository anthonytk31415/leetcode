
def minPairSum(nums): 
    nums.sort()
    i = 0
    j = len(nums) - 1
    res = -inf
    while i < j: 
        res = max(res, nums[i] + nums[j])
        i += 1
        j -= 1
    return res