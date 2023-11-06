# house robber
# 24 min
# time: O(N)
# spaace: O(N)

def rob(nums):

    c = {}
    c[-1]= 0
    c[0] = nums[0]
    c[1] = max(nums[0:2])

    for i in range(2,len(nums)):
        c[i] = max(nums[i] + c[i-2], c[i-1])
    return c[len(nums)-1]

# nums = [1,2,3,1]
nums =[2,7,9,3,1]
print(rob(nums))