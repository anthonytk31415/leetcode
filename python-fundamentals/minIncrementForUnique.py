
from collections import defaultdict, OrderedDict

def minIncrementForUnique1(nums):
    nums.sort()
    counter = OrderedDict()
    for x in nums: 
        if x not in counter: 
            counter[x] = 1
        else: 
            counter[x] +=1
    
    # keep j at least at i or after and increment j so it is at the smallest index where counter[j] == 0
    res = 0
    j = 0
    for i in counter:
        j = max(i + 1, j)
        while counter[i] > 1:
            if j not in counter:
                
                counter[j] +=1
                res += (j - i)
                j +=1
                counter[i] -= 1
            else: 
                j +=1
        i +=1
    return 

def minIncrementForUnique(nums):
    nums.sort()
    res = 0
    print(nums)
    for i in range(1, len(nums)):
        if nums[i] <= nums[i-1]:
            res += (nums[i-1] - nums[i] + 1)
            nums[i] = nums[i-1] + 1
    return res

nums = [3,2,1,2,1,7]
print(minIncrementForUnique(nums))