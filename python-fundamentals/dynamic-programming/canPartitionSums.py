# def canPartition(nums):
#     if sum(nums) % 2 == 1: 
#         return False
#     target = sum(nums)/2
#     memo = {}
#     nums.sort()
#     def helper(nums, target, i):
#         if (target, i) in memo: 
#             return memo[(target, i)]
#         else: 
#             res = None
#             if target == 0: 
#                 res = True
#             elif target < 0: 
#                 res = False 
#             else: 
#                 res = any([helper(nums, target - nums[j], j+1) for j in range(i, len(nums))])
#             memo[(target, i)] = res
#             return res
                
#     if helper(nums, target, 0): 
#         return True
#     else: 
#         return False

# here you start with a set with the first item from nums
# you then iterate 


def canPartition(nums):
    t = sum(nums)/2
    P = set([nums[0]])
    for x in nums[1:]:
        for y in list(P):
            P.add(x+y)
    return t in P



# nums = [1,5,11,5]
# nums = [1,2,3,5]

nums = [35,69,8,10,56,85,20,67,39,15,57,19,80,45,12,81,92,98,25,26,51,3,31,16,30,37,55,52,61,17,30,82,52,85,84,83,98,29,79,29,99,70,97,20,42,22,44,44,65,75,70,86,97,100,45,69,91,53,88,96,65,88,92,73,16,57,34,11,64,3,92,48,98,29,39,16,47,92,22,19,50,86,78,68,52,51,70,80,2,58,79,70,91,94,23,47,81,4,18,15]
## is there a subset whose sum equals target? 

# Time: O(2^n)

# print(sum(nums))
print(canPartition(nums))
