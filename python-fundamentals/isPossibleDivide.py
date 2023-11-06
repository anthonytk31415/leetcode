
# Time O(n log n)
# Space O(n) for the orderedict

# sort the nums and then add them to an ordered dict to create a count.
# create a loop where you start with the first key in the dict and you find whether the key plus the next k - 1 numbers ( by adding 1 to the key each time) are in the dict 
# When there is, decrement the dict[i] by 1 or delete to remove out of the ordered dict. 
# during the loop, if you don't find that next number, return False. 
# Do that cycle K times until the ordereddict is empty. 

# we keep an ordereddict to ensure that we can take the smallest index every time

from collections import OrderedDict


def isPossibleDivide(nums, k):
    if len(nums) % k != 0: 
        return False
    
    nums.sort()

    countNums = OrderedDict()
    
    for x in nums: 
        if x not in countNums: 
            countNums[x] =1
        else: 
            countNums[x] +=1
        
    while countNums:
        for key in countNums:
            for i in range(key, key + k):
                if i in countNums:
                    if countNums[i] == 1: 
                        del countNums[i]
                    else: 
                        countNums[i] -=1
                else: 
                    return False
            break
    return True

# nums = [3,2,1,2,3,4,3,4,5,9,10,11]
# k = 3

# nums =[1,1,1,2,2,2,3,3,4] 
# k = 3

nums =[1,1,1,2,2,2,3,3,3] 
k = 3

print(isPossibleDivide(nums, k))