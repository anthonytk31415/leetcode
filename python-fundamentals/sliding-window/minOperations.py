from math import inf

# sort and sliding window approach: nlogn

def minOperations(nums):
    if len(nums) <= 1: return 0
    delta = len(nums) - 1

    nums.sort()
    
    numAudit = [None for _ in range(len(nums))]
    endingJ = [None for _ in range(len(nums))]

    i = 0
    j = 0
    counter = 0
    maxCounter = -inf
    while i < len(nums) and j < len(nums):
        if i == j: 
            j += 1
        while True: 
            if (j < len(nums)) and (nums[j] - nums[i] <= delta): 
                if nums[j] != nums[j-1]:
                    counter += 1
                j += 1
            else: 
                break
        
        numAudit[i] = counter
        maxCounter = max(maxCounter, counter)
        i += 1
        if i < len(nums) and nums[i] != nums[i-1]:
            counter -= 1
            counter = max(0, counter)


    # print(numAudit)
    return len(nums) - maxCounter - 1


# nums = [1,10,100,1000]
# nums = [4,2,5,3]
# nums = [1,2,3,5,6]
# nums = [1,2,6,7,10,11]



# nums = [8,5,9,9,8,4]

# nums = [44,28,33,49,4,2,35,28,25,38,47,20,14,30,27,38,42,14,34]

nums = [6871,3056,8843,3642,4544,300,6054,6345,2161,1107,1957,6273,2799,6665,2000,1483,3148,1655,7468,4904,9195,9500,7041,7335,8494,386,7754,8739,6893,1015,6411,641,4631,6156,7146,4461,9517,960,7328,5314,3846,9943,59,3310,9637,3296,7056,4873,5226,3943,5488,4193,8906,259,626,9800,9725,8610,901,2467,3722,9322,9500,1348,8727,5618,8641,6579,9689,1776,6421,7690,6414,8600,4285,3513,3210,7290,8918,882,2099,6472,4902,553,6420,4586,3478,5130,7785,3679,2301,5460,4285,9409,1160,7447,3127,8771,9863,9452,9879,207,3792,5044,9256,8011,8119,8815,6762,2255,3754,4301,5534,5667,3672,1063,4667,7711,6225,9914,7845,1180,7461,6807,7219,5071,3185,8433,2367,3397,1608,7779,3893,4172,4470,2793,502,4781,2659,7601,784,2267,5121,9394,2582,3479,4087,2110,7723,6859,3423,1512,9040,2479,1704,8963,7801,6430,4575,2263,3525,3325,3491,476,8585,3243]


print(len(nums))
print(sorted(nums))
print(minOperations(nums))