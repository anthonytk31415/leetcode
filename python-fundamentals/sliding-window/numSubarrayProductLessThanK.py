# sliding glide 

def numSubarrayProductLessThanK(nums, k):
    res = 0
    right = 0
    curProduct = nums[0]
    for left in range(len(nums)):
        right = max(right, left)
        if left == right: curProduct = nums[left]
        else: curProduct /= nums[left - 1]
        while right + 1 < len(nums) and curProduct*nums[right + 1] < k: 
            right += 1
            curProduct *= nums[right ]

        if curProduct < k: 
            res += right - left + 1
    return res

# nums = [10,5,2,6]
# k = 100

# nums = [1,2,3]
# k = 0

# nums = [2,3,4,5,1]
# k = 20


nums = [10,9,10,4,3,8,3,3,6,2,10,10,9,3]
k = 19

print(numSubarrayProductLessThanK(nums, k))