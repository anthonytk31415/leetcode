




# time: O()
# complexity: O()

def permute(nums):
    if len(nums) == 1:
        return [nums]
    res = []
    for i in range(len(nums)):
        x = nums[i]
        newNums = nums[:i] + nums[i+1:]
        for y in permute(newNums):
            res.append([x]+y)
    return res

nums = [1,2,3]

print(permute(nums))

from itertools import permutations

def permute2(nums):
    return [list(x) for x in permutations(nums)]


print(permute2(nums))