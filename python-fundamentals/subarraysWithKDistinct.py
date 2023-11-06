# lets do brute force n^2 


# this is going to be too slow
def subarraysWithKDistinct0(nums, k):
    counter = 0 
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)+1):
            if len(set(nums[i:j])) == k:
                counter +=1
    return counter

nums = [1,2,1,2,3]
k = 2

# nums = [1,2,1,3,4]
# k = 3

# nums = [1,2,1,3,4]
# k = 1

print(subarraysWithKDistinct0(nums, k))