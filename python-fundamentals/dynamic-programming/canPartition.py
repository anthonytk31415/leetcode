def canPartition(nums):
    c = []
    for x in nums: 
        x_new = [x]
        c = c + [[z + x_new] for z in c]
    return c

print(canPartition([1,2]))