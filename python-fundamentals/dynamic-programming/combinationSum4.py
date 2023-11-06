
#this returns the right combinations but it is too slow or takes up too much memory
# def combinationSum4(nums, target):
#     memo = {0:[[]],}
#     for t in range(1, target+1):
#         cur_res = []        
#         for x in nums: 
#             if t-x >= 0: 
#                 for z in memo[t-x]:
#                     forward = z + [x]
#                     backward = [x] + z
#                     if forward not in cur_res: 
#                         cur_res.append(forward)
#                     if backward not in cur_res: 
#                         cur_res.append(backward)
#         memo[t] = cur_res
#     return len(memo[target])


# Time = O(t*n)
# this takes O(target) space to memozie each t from 0, .. target

def combinationSum4(nums, target):
    ans = [0]*(target+1)            # this represents how many combinations for t = 0, 1, ..., target
    for x in nums:
        ans[x] +=1                  # initiate with when the num == target 
    for t in range(1, target + 1):
        temp = 0                    # we got bottoms-up for t > (1 to target) to find # combinations that will add to target
        for y in nums:              # by taking (t - num) for each num in nums and using ans(t-num) to memoize
            if t - y >0:            # and summing those answers for each target
                temp +=ans[t-y]     # You need to prove this on paper to understand that logic  
        ans[t] += temp              
    return ans[target]

print(combinationSum4([1,2,3], 4))