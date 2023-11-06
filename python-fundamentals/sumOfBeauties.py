from math import inf

# Time and Space: O(n)

def sumOfBeauties(nums):

    minRight = [inf] * len(nums)
    maxLeft = [-inf] * len(nums)
    is_one = [0] * len(nums)
    is_two = [0] * len(nums)

    # build is_one
    for i in range(1, len(nums)-1):
        if nums[i - 1] < nums[i] < nums[i + 1]:
            is_one[i] = 1
    
    # mins and maxes

    # maxLeft
    for i in range(1, len(nums)):
        maxLeft[i] = max(maxLeft[i-1], nums[i-1]) 

    #minRight
    for i in range(len(nums)-2, 0, -1):
        print(i)
        minRight[i] = min(minRight[i+1], nums[i+1])

    # build is_two
    for i in range(1, len(nums)-1):
        if maxLeft[i] < nums[i] < minRight[i]:
            is_two[i] = 2

    cumSum = 0
    for i in range(1, len(nums)-1):
        cumSum += max(is_one[i], is_two[i])


    return cumSum

    # print(is_two)
    # print(f'minRight = {minRight}')
    # print(f'maxleft = {maxLeft}')

# nums = [2,4,6,4]
nums = [1,2,3]
print(sumOfBeauties(nums))