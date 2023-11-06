
## rotate the array till you find it
# def findMin(nums):
#     if len(nums) == 1:
#         return nums[0]
#     for i in range(1,len(nums)):
#         if nums[i-1] > nums[i]:
#             return nums[i]
#     return nums[0]

# print(findMin([3,4,5,1,2]))

x = [4,5,6,7,0,1,2]

# print(findMin(x))





# def findMin(nums):
#     if len(nums) == 1:
#         return nums[0]
#     if len(nums) == 2:
#         if nums[0] > nums[-1]:
#             return nums[-1]
#     if nums[0] < nums[-1]:
#         return nums[0]
#     mid = len(nums) // 2 -1
#     if nums[mid] > nums[mid + 1]:
#         return nums[mid+1]
#     elif nums[0] > nums[mid]:
#         return findMin(nums[:mid+1])
#     else: 
#         return findMin(nums[mid+1:])


def findMin(nums):
    left = 0
    right = len(nums) - 1
    while left < right: 
        mid = (left + right)//2 
        if nums[right]< nums[mid]:
            left = mid + 1
        else: 
            right = mid
    return nums[left]



# x = [3,4,5,1,2]
x = [4,5,6,7,0,1,2]
print(findMin(x))