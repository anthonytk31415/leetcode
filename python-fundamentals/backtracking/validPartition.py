# This backtracking is too slow. Let's use DP
def validPartition1(nums):

    def dfs(i):
        if i >= len(nums): return True
        if i+2 < len(nums) and nums[i] == nums[i+1] and nums[i] == nums[i+2] and dfs(i+3): return True
        if i+1 < len(nums) and nums[i] == nums[i+1] and dfs(i+2): return True
        if i+2 < len(nums) and nums[i] +1 == nums[i+1] and nums[i+1] + 1 == nums[i+2] and dfs(i+3): return True 
        return False
    
    return dfs(0)

from math import inf 

# Use DP!
# Lets use constant space; previously, I used a dp the length of nums. but you're really 
# only interested in the prior 4 entries. 
# Time: O(n), Space: O(1)

def validPartition(nums):
    nums = [-inf] + nums
    dp = [False]*4
    for i in range(len(nums)):
        if ((i == 0) or 
            (i-3 >= 0 and dp[-1-3] == True and nums[i] == nums[i-1] and nums[i] == nums[i-2]) or 
            (i-3 >= 0 and dp[-1-3] == True and nums[i] == nums[i-1]+1 and nums[i-2]+2 == nums[i]) or 
            (i-2 >= 0 and dp[-1-2] == True and nums[i] == nums[i-1])):
            dp[-1] = True
        if i != len(nums) - 1: 
            dp[0], dp[1], dp[2], dp[3] = dp[1], dp[2], dp[3], False

    return dp[-1]

nums = [4,4,4,5,6]
# nums = [1,1,1,2]
nums = [993335,993336,993337,993338,993339,993340,993341]
print(validPartition(nums))