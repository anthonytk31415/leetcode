from math import inf

def findPeakElement(nums):
    
    nums = [-inf] + nums + [-inf]
    left = 1
    right = len(nums) - 2


    while (not (nums[left - 1] < nums[left] and nums[left] > nums[left + 1]) or 
          not (nums[right - 1] < nums[right] and nums[right] > nums[right + 1])):

        mid = (left + right) // 2

        if (nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]): return mid - 1

        if nums[mid -1] > nums[mid + 1]: right = mid-1
        else: left = mid + 1

    if nums[left - 1] < nums[left] and nums[left] > nums[left + 1]: return left - 1
    else: return right - 1

nums = [1,2,1,3,5,6,4]
nums = [1,2,3,1]
print(findPeakElement(nums))