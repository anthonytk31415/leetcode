from collections import deque 

def minimumArrayLength(nums):
    nums.sort()
    res = 0
    nums = deque(nums)
    while len(nums) > 1: 
        a, b = nums[0], nums[-1]
        if a % b == 0: 
            res += 1
            nums.popleft()

        nums.pop()


    return res + len(nums)

nums = [5,2,2,2,9,10]
# nums = [1,4,3,1]
# nums = [5,5,5,10,5]
# nums = [2,3,4]
print(minimumArrayLength(nums))

# print(4%1)
# # print(3%0)

# print(6%4)

# print(5 % 10)


