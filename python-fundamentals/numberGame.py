def numberGame(nums):
    nums.sort()
    arr = []
    for i in range(0, len(nums), 2):
        arr.append(nums[i+1])
        arr.append(nums[i])
    return arr

nums = [5,4,2,3]
nums = [2,5]
print(numberGame(nums))