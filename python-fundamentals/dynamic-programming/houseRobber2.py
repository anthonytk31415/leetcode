## refer to p, r as indexes, and then "adjust"

from functools import lru_cache

def rob(nums):
    from collections import defaultdict
    memo = {}

    def helper(nums, p, r, memo):
        if (p,r) in memo: 
            return memo[(p,r)]
        if p > r:
            ans = 0
        elif 0 <= r-p <=1:
            ans = max(nums[p:r+1])
        else: 
            ans = max(nums[p] + helper(nums, p+2, r, memo), 
                      nums[p+1] + helper(nums, p+3, r, memo))
        
        memo[(p,r)] = ans
        return ans

    if len(nums) == 0:
        return 0
    if 1 <= len(nums) <= 3: 
        return max(nums)
    else:  
        end = len(nums) - 1
        return max(nums[0] + helper(nums, 2, end-1, memo), 
                   nums[1] + helper(nums, 3, end, memo), 
                   nums[end] + helper(nums, 1, end - 2, memo))


## lets add a memo here



    #helper will allow us to recurively take smaller arrays used on non-cycle arrays


# print(rob([2,3,1]))
# print(rob([2,3,2]))
# # print(rob([1,2,3]))

# print(rob([1,2,3,1]))


# print(rob([2,3,2,5,3,2,4,7]))

# time: O(n)
# space: O(1)

## either you take the n0 and bests from (2:-1), or you take n1 and bests from (3:)
# for the helper, 
# - initiate two pointers and set them to 0. 
# - Iterate over the nums.
# before current iteration updating:   
# dp1 (for i - 1)= best option i - 2; when overwritten, dp1 = dp2 at i
# dp2 (for i - 1)= best option at i - 1; when overwrittedn, dp2 = max( dp1 at i -1 + current num, dp2 at i - 1); note dp1 at i -1 = dp2 at i - 2
#     (1) from prior iteration 
#     (2) best option from prior/prior + addition at current iteration

def rob2(nums):
    def helper(nums):
        dp1, dp2 = 0, 0
        for num in nums:
            dp1, dp2 = dp2, max(dp1 + num, dp2) 
        return dp2
    return max(nums[0] + helper(nums[2:-1]), 
               nums[1] + helper(nums[3:]))

print(rob2([200,3,140,20,10]))