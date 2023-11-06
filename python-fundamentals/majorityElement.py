# this solution is linear time and space

from collections import Counter

def majorityElement(nums):
    numCount = Counter(nums)
 
    threshold = len(nums) // 3
    res = set()
    for x in numCount: 
        if numCount[x] > threshold: 
            res.add(x)

    return res

print(majorityElement([3,2,3]))


# how do you solve this in linear time and constant space? 


