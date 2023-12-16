# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/?envType=daily-question&envId=2023-12-14

    # binary search for the max
    # then divide the interval in two
    # then binary searc for num in both intervals


def search(nums):
    left = 0
    right = len(nums) - 1
    while left <= right: 

        mid = (left + right) // 2
        while left < mid and nums[left] == nums[mid]:
            left += 1
        if nums[mid] == target:
            return True
        if nums[left] <= nums[mid]:
            if nums[left] <= target <= nums[mid]: 
                right = mid - 1
            else: 
                left = mid + 1

        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else: 
                right = mid - 1

    return False


nums = [4,4,4,5,4]
target = 5

# nums = [8, 9, 10, 10, 11,0,1,2,3,3,3,3,3,4,4,4,4,4,5,6]
# target = -5

# nums = [2,2,2,0,0,1]
# target = 0
# nums = [1,0]
# target = 0

print(search(nums))