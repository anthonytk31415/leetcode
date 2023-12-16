def search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right: 
        if left == right and nums[left] != target: break 
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= target <= nums[mid - 1]:
            right = mid - 1
        else: 
            left = mid + 1



    return - 1



nums = [20, 23, 100, 101, 2,3,4,5,6, 10, 11, 13]
target = 13

nums = [3,4,5,6,1,2]
target = 2


nums = [3,4,5,6,7,8,1,2]
target = 2
# nums = [6,7,1,2,3,4,5]
# target = 6

print(search(nums, target))