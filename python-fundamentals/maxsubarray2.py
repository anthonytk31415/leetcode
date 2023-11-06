## this is a dynamic problem; 
# the trick is to see that as you traverse through the array nums, 
# at each step, the answer is dependent on the prior step
# and the prior step calculates whether the prior contributes to increasing the sum
# (e.g. if it's negative, then prior = 0; if prior > 0, then you add it to the num[i])
# you also evaluate the max at every given step: between the prev max and the value currently

## this is succinct, but not fast enough.. lets suppress
def maxSubArray(nums):
    res = nums[0]
    for i in range(1,len(nums)):
        prior = 0
        prior = nums[i-1]
        if prior < 0: prior = 0
        tmp = prior + nums[i]
        nums[i] = tmp
        if tmp > res: res = tmp
    return res

nums = [-2,1,-3,4,-1,2,1,-5,4]

# nums = [5,4,-1,7,8]

print(maxSubArray(nums))



# def maxSubArray(nums):
#     prior = max(0,nums[0])
#     res = nums[0]
#     for x in nums[1:]:
#         b = x + prior
#         print(x, prior, b)
#         res = max(res, b)
#         # set up for next iteration
#         prior = max(0,b)
#     return res