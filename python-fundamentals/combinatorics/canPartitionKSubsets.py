from collections import deque
def canPartitionKSubsets(nums, k):
    nums.sort(key = lambda x: -x)
    if sum(nums) % k != 0: return False
    subsetSum = sum(nums) / k 

    # 

    # sumNums will be tracking the sum if each kth subgroup
    # j is the index of nums you'll iterate over
    # each dfs cycle you'll add num[j] across the some kth group and assess
    # if you're over 
    def dfs(j):
        if j == len(nums): return True
        for idx in range(k):
            if sumNums[idx] + nums[j] <= subsetSum: 
                sumNums[idx] += nums[j]
                if dfs(j+1): 
                    return True
                sumNums[idx] -= nums[j]
                if sumNums[idx] == 0: 
                    break

                    
        return False
    sumNums = [0 for _ in range(k)]

    return dfs(0) 


nums = [4,3,2,3,5,2,1]
k = 4

# nums = [3522,181,521,515,304,123,2512,312,922,407,146,1932,4037,2646,3871,269]
# k = 5

nums = [18,20,39,73,96,99,101,111,114,190,207,295,471,649,700,1037]
k = 4

nums = [1,1,2,4]
k = 4


# nums = [10,1,10,9,6,1,9,5,9,10,7,8,5,2,10,8]
# k = 11
print(canPartitionKSubsets(nums, k))