
#this is currently O(2^n); how to minimize? use a memo. 


def findTargetSumWays(nums, target):
    memo = {}
    # iterate through all possibilities of test
    def helper(nums, target, memo):
        if not nums: 
            if target == 0: 
                return 1
            else: 
                return 0
        else: 
            z = (tuple(nums), target) 
            if z in memo:
                return memo[z]
            else: 
                res = (helper(nums[1:], target + nums[0], memo) + helper(nums[1:], target - nums[0], memo))

                memo[z] = res
                return res

    return helper(nums, target, memo)


nums = [1,1,1,1,1]
target = 3


# nums = [1] 
# target = 1
print(findTargetSumWays(nums, target))