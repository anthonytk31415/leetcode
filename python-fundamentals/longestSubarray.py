# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/submissions/988016148/

def longestSubarray(nums):
    if len(nums) <= 1:
        return 0

    arr = []
    num = nums[0]
    nums_count = 1
    for i in range(1, len(nums)):
        cur = nums[i]
        if cur == num: 
            nums_count +=1
        else:
            arr.append([num, nums_count])
            num = cur
            nums_count = 1

    arr.append([num, nums_count])

    # print('1:', arr)

    if len(arr) == 1:
        if arr[0][0] == 1:
            return arr[0][1] - 1
        else: 
            return 0
    
    res = 0
    for i in range(len(arr)):
        cur_res = 0
        if arr[i][0] == 0: 
            left = 0
            if i - 1 >= 0: left = arr[i-1][1]
            right = 0
            if i + 1  < len(arr): right = arr[i + 1][1]

            if arr[i][1] == 1: cur_res = left + right
            else: cur_res = max(left, right)

        res = max(res, cur_res)

    return res


# nums = [1,1,1]
# nums = [0,0,0]
# nums = [1,1,0,1]
nums = [0,1,1,1,0,1,1,0,1]

print( 'the ans is:', longestSubarray(nums))