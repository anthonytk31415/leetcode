
# Interesting two pointer question. It's not O(n) though. You must traverse the entire 0 to i-1 interval.

def triangleNumber(nums):
    if len(nums) <= 2: return 0

    nums.sort()
    res = 0
    for i in range(2, len(nums)):
        left, right = 0, i - 1
        while left < right: 
            if nums[left] + nums[right] > nums[i]:
                res += right - left
                right -= 1
            else: 
                left += 1
            
    return res

nums = [2,2,3,3,4]
print(triangleNumber(nums))