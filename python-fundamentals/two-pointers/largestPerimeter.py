def largestPerimeter(nums):
    nums.sort()
    i = len(nums) - 1
    curSum = sum(nums)
    while i >= 2: 
        curSum -= nums[i]
        if curSum > nums[i]:
            return curSum + nums[i]
            break 
        i -= 1
    return -1

nums0 = [5,5,5]
nums1 = [1,12,1,2,5,50,3]
nums2 = [5,5,50]

for nums in [nums0, nums1, nums2]:
    print(largestPerimeter(nums))