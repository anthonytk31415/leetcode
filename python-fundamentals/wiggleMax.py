from collections import deque

# here we use a deque for easy keeping track; we modify below for O(1) space
def wiggleMaxLength1(nums):
    # trivial cases ; can probably do some optimiations with space here using indexes
    nums = deque(nums)    
    while len(nums) > 1 and nums[0] == nums[1]: 
        nums.popleft()

    if len(nums) == 1: 
        return 1
    if len(nums) == 2 and nums[0] != nums[1]:
        return 2

    def direction(u, v):
        if nums[u] < nums[v]:
            return "pos"
        elif nums[u] > nums[v]:
            return "neg"
        else: 
            return "equ"

    dirInc = "tbd"
    countWiggles = 2
    for i in range(1, len(nums)):
        curDir = direction(i-1, i)
        if curDir == "equ": continue
        if dirInc != "tbd" and curDir != dirInc: 
            countWiggles += 1
        dirInc = curDir 
    
    return countWiggles


# First we move up the start from 0 to wheenver we dont see consecutive equals
# Then we check for trivial answers. 
# Then we have a guaranteed length of 2. We now check for "wiggles" i.e. when 
# the direction changes. 

# O(1) space, O(n) Time for traversing once

def wiggleMaxLength(nums):
    # trivial cases ; can probably do some optimiations with space here using indexes
    start = 0
    while len(nums) - start > 1 and nums[start] == nums[start + 1]: 
        start += 1

    if len(nums) - start == 1: 
        return 1
    if len(nums) - start == 2 and nums[start] != nums[start + 1]:
        return 2

    def direction(u, v):
        if nums[u] < nums[v]:
            return "pos"
        elif nums[u] > nums[v]:
            return "neg"
        else: 
            return "equ"

    dirInc = "tbd"
    countWiggles = 2
    for i in range(start + 1, len(nums)):
        curDir = direction(i-1, i)
        if curDir == "equ": continue
        if dirInc != "tbd" and curDir != dirInc: 
            countWiggles += 1
        dirInc = curDir 
    
    return countWiggles




# nums = [1,7,4,9,2,5]
# nums = [1,17,5,10,13,15,10,5,16,8]
nums = [1,2,3,4,5,6,7,8,9]
# nums = [0,0]
print(wiggleMaxLength(nums))