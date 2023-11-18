# https://leetcode.com/problems/frequency-of-the-most-frequent-element/?envType=daily-question&envId=2023-11-18

# here is a two pointers solution
def maxFrequency1(nums, k):
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
    return maxCount

# here is a sliding window solution
def maxFrequency(nums, k):
    nums.sort()
    left = 0
    right = len(nums) - 1
    totalSum = sum([nums[right] - curLeft for curLeft in nums])
    while totalSum > k: 
        totalSum -= nums[right] - nums[left]
        left += 1
    maxCounter = right - left + 1 

    for right in range(len(nums)-2, -1, -1):
        width = right - left + 1
        delta = nums[right + 1] - nums[right]
        totalSum -= width*delta
        while left > 0:
            if totalSum + (nums[right] - nums[left - 1]) <= k:
                totalSum += (nums[right] - nums[left - 1])
                left -= 1
            else: break
        maxCounter = max(maxCounter, right - left + 1)
    return maxCounter





# nums = [9968,9934,9996,9928,9934,9906,9971,9980,9931,9970,9928,9973,9930,9992,9930,9920,9927,9951,9939,9915,9963,9955,9955,9955,9933,9926,9987,9912,9942,9961,9988,9966,9906,9992,9938,9941,9987,9917,10000,9919,9945,9953,9994,9913,9983,9967,9996,9962,9982,9946,9924,9982,9910,9930,9990,9903,9987,9977,9927,9922,9970,9978,9925,9950,9988,9980,9991,9997,9920,9910,9957,9938,9928,9944,9995,9905,9937,9946,9953,9909,9979,9961,9986,9979,9996,9912,9906,9968,9926,10000,9922,9943,9982,9917,9920,9952,9908,10000,9914,9979,9932,9918,9996,9923,9929,9997,9901,9955,9976,9959,9995,9948,9994,9996,9939,9977,9977,9901,9939,9953,9902,9926,9993,9926,9906,9914,9911,9901,9912,9990,9922,9911,9907,9901,9998,9941,9950,9985,9935,9928,9909,9929,9963,9997,9977,9997,9938,9933,9925,9907,9976,9921,9957,9931,9925,9979,9935,9990,9910,9938,9947,9969,9989,9976,9900,9910,9967,9951,9984,9979,9916,9978,9961,9986,9945,9976,9980,9921,9975,9999,9922]
# k = 1524

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
