# Time: O(n)
# space: O(n)


def findUnsortedSubarray(nums):
    nums_s = sorted(nums)
    minmax = [None, None] ## [min, max]
    
    for i in range(len(nums)):
        if nums[i] != nums_s[i]:
            minmax[0] = i
            break
    for j in range(len(nums)-1, -1, -1):
        if nums[j] != nums_s[j]:
            minmax[1] = j
            break
    # print(minmax)
    if minmax == [None, None]: 
        return 0
    return minmax[1] - minmax[0] + 1


# nums = [2,6,4,8,10,9,15]
nums = [1, 5]
print(findUnsortedSubarray(nums))