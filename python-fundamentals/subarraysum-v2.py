from collections import defaultdict

# our goal is to keep a running sum. 
# we want to find all x such that: 
    # running_sum_x + target_sum = running_sum_y
    # which means from x to y, you achieve target sum 
# after performng the check, we save the results of each running sum in a hash table

# time: O(n)
# space: O(n)

def subarraySum(nums, k):
    count = 0
    runningSum = 0
    runnings = defaultdict(int)
    runnings[0] +=1
    for num in nums: 
        runningSum += num
        if (runningSum - k) in runnings: 
            count += runnings[runningSum - k]
        runnings[runningSum] +=1
    return count

nums = [1,2,3]
k = 3

# nums = [1,1,1]
# k = 2

# nums = [1]
# k = 0

print(subarraySum(nums, k))