## binary search
## search for the divisor
# - the right pointer will always be a candidate for the answer. 
# - we'll go through the loop when left < right (<= as when left = right, we'll return right)/
# - when the sum_res <= threshold, we put the right = mid; note that right will always be a candidate
# - if sum_res > threshold, we've overshot and left = mid + 1

# time: O(nlogn)
# space: O(1)

from math import ceil

def smallestDivisor(nums, threshold):


    left = 1
    right = max(nums)
    if threshold == len(nums):
        return right

    while left < right: 
        mid = (left + right) // 2
        sum_res = sum([ceil(x/mid) for x in nums])
        if sum_res <= threshold: 
            right = mid 
        elif sum_res > threshold:
            left = mid + 1

    return right


nums = [1,2,5,9]
threshold = 6

print(smallestDivisor(nums, threshold))

# lets think of edge cases