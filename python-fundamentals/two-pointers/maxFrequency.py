# https://leetcode.com/problems/frequency-of-the-most-frequent-element/?envType=daily-question&envId=2023-11-18


# some sort of cumulative sum

# sort the array
# then built an array where the ith element equals delta from i-1 to i; call this arr = delta 
# then start from the end of the array and keep a running sum
# - call this j that starts from len(arr) - 1
# - and iterate until j = 0 (you can't change anything to get to the min element, which is at j = 0)

# - keep a running sum that starts at i = len(arr) - 1
# - running sum = 0; counter = 0
# - if running sum + delta[i] <= k: 
#     runningSum = runningSum + delta[i]
#     counter += 1
# - else: at this state, you cannot increment anymore. so 


# k = 4
# 1 3 4 8 9 11 = arr
#   2 1 4 1 2  = delta
          

# ans = 3


def maxFrequency(nums, k):
    nums.sort()

    i, j = len(nums) - 1, len(nums) - 1
    maxCount, curCount = 1, 1
    # i = current anchor
    # j = last index "taken"
    while j >= 1: 
        # can j - 1 be taken from i? 
        delta = nums[i] - nums[j-1]
        if delta <= k: 
            k -= delta 
            j -= 1
            curCount += 1
            maxCount = max(maxCount, curCount)
        else: 
            if i > j: 
                addBack = (i - j) * (nums[i] - nums[i-1])
                k += addBack
                curCount -= 1
            else: 
                j -= 1
            i -= 1  
        print("i", i, "j", j, "curcount", curCount, "k", k)
    return maxCount

nums = [9930,9923,9983,9997,9934,9952,9945,9914,9985,9982,9970,9932,9985,9902,9975,9990,9922,9990,9994,9937,9996,9964,9943,9963,9911,9925,9935,9945,9933,9916,9930,9938,10000,9916,9911,9959,9957,9907,9913,9916,9993,9930,9975,9924,9988,9923,9910,9925,9977,9981,9927,9930,9927,9925,9923,9904,9928,9928,9986,9903,9985,9954,9938,9911,9952,9974,9926,9920,9972,9983,9973,9917,9995,9973,9977,9947,9936,9975,9954,9932,9964,9972,9935,9946,9966]
k = 3056

# nums =  [1, 3, 4, 8, 9, 11]
# k = 4

# nums = [1,4,8,13]
# k = 5

# 73
# nums = [1,2,4]
# k = 5

# nums = [3,9,6]
# k = 2


# nums = [1,3,5,7,7,7 ,8,9]
# k = 5


# nums.sort()
# print(nums)
print("len nums: ", len(nums))
print(maxFrequency(nums, k))
