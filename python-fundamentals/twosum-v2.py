# twosum-v2

# sorted --> O(nlogn)
# len is O(1) time complexity

# this is done in O(n) time, with 

# since you can't use the item twice, you only need to fill the dictionary once and pass through the array once. 
# hence the commneted area where you fill the dictionary once is unneeded. 


def twosum(nums, target):
    numSet = {}
    # for i in range(len(nums)):
    #     n = nums[i]
    #     if n not in numSet:
    #         numSet[n] = [i]
    #     else: 
    #         numSet[n].append(i)
    # print(numSet)
    for i, n in enumerate(nums):
        x = target - n
        if x in numSet: 
            return[i, numSet[x]]
        else: 
            numSet[n] = i

        


# min
# max
# - if target < 

a = [3,2,4]

b = twosum(a, 6)
print(b)
# target = -13
# - contains 0
# - if target > max and positive --> pairs need to be positive
# - if target < min and negative --> pairs need to be negative

# x1, x2 pairs
# target - x1 > 0: examine positives
# target - x1 < 0: examine negatives 

# [1,3,5,7]
# - all positive
# - if target < 0 impossible




# [-20,-10,-4,-3,-2]
# - all negative
# - if 



## twosum v3


# use a hash set track target - nums[i]
# target - nums[i] in hash set (from a previous iteration), append that answer to your result
# if not, create that hash set element: 

def twoSum2(nums, target):
    cache = {}                          # contains key = num in nums; val = index in nums
    for i in range(len(nums)): 
        z = target - nums[i]
        if z in cache: 
            return [i, cache[z]]
        else: 
            cache[nums[i]] = i

nums = [1,2,3]
target = 4
print(twoSum2(nums, target))
