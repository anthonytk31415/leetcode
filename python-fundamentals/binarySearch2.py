# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         def binarySearch(nums, left, right, target):
#             if left == right:
#                 if nums[left] == target: return left
#                 else: return -1
#             if left > right: 
#                 return -1

#             q = (left + right) // 2             
#             if nums[q] == target: 
#                 return q
#             elif nums[q] > target: 
#                 return binarySearch(nums, left, q-1, target)
#             else:
#                 return binarySearch(nums, q+1, right, target)
#         return binarySearch(nums, 0, len(nums)-1, target)

from bisect import bisect

def binary2(nums, target):

    idx = bisect(nums, target)
    if 0 <= idx - 1 <= len(nums)-1 and nums[idx-1] == target: 
        return idx-1
    return -1


nums = [1,2,3,4,6,7]
target = 5

# print(search(nums, target))
print(binary2(nums, target))