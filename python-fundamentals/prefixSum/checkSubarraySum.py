
# main concept is if nums[i:j] % k == 0 for some i < j then nums[:i] % k == nums[i:j] %k. 
# This is because the portion from [i:k] %k = 0, and you are left with the portion from [:i]. 

# so we instantiate a tracker with 0 : -1 to indicate 0 has been scanned before in case we see that the sum is
# 0, which is allowable, and each iteration, we check if the prefixSum is in the tracker and also, 
# whether the current index - the earliest index of that tracker[remainder] > 1 (i.e. we have length at least 2).abs

# Here we have O(N) time and space!

def checkSubarraySum(nums, k ):
    curSum = 0
    tracker = {0: -1}
    for i in range(len(nums)):
        curSum += nums[i] 
        mod = curSum % k 
        if mod in tracker and i - tracker[mod] > 1: 
            # print(tracker)
            return True
        if mod not in tracker:
            tracker[mod] = i
    # print(tracker)
    return False
 
nums = [23,2,4,6,7]
k = 6

nums = [23,2,4,6,6]
k = 7

# nums = [1,2,12]
# k = 6

# nums = [5,0,0,0]
# k = 3

# nums = [1,2,3]
# k = 5

# nums = [0]
# k = 1

print(checkSubarraySum(nums, k ))