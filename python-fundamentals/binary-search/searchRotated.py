def search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right: 

        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] < nums[mid]:
            if nums[left] <= target <= nums[mid]: 
                right = mid - 1
            else: 
                left = mid + 1

        elif nums[mid] < nums[right]:
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else: 
                right = mid - 1
        else: 
            left += 1
    return -1

# nums = [1]
# target = 2

# nums = [3, 1]
# target = 1

# nums = [4, 1,2,3]
# target = 4
nums = [20, 23, 100, 101, 2,3,4,5,6, 10, 11, 13]
target = 13

# nums = [3,4,5,6,1,2]
# target = 2

# nums = [3,4,5,6,7,8,1,2]
# target = 2
# nums = [6,7,1,2,3,4,5]
# target = 6

print(search(nums, target))