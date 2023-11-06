
## can have negative values 
## https://www.geeksforgeeks.org/prefix-sum-array-implementation-applications-competitive-programming/



def subarraySum(nums, k): 
    sums = [0]*len(nums)



# nums = [1,1,1]
# k = 2

# nums = [1,2,3]
# k = 3

nums = [11]
k = 0


print(subarraySum(nums, k))



            # if k == 0: 
            #     res = 1
            # elif len(nums) == 1 and nums[0] < k:
            #     res = 0
            # elif k < 0:  
            #     res = 0
            # elif len(nums) == 0 and k != 0: 
            #     res = 0
            # else: 
            #     res = 0
            #     if chain: 
            #         res += helper(nums[1:], k_star, k_star, memo, True)
            #     res += helper(nums[1:], k - nums[0], k_star, memo, False) 
            # memo[tuple(nums), k] = res