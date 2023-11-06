def subsetsWithDup(nums):
    nums.sort()
    res = [[]]
    for x in nums: 
        res = res + [y + [x] for y in res]
    res1 = set()
    for y in res: 
        y = tuple((y))
        if y not in res1: 
            res1.add(y)

    return res1
nums = [4,4,4,1,4]
print(subsetsWithDup(nums))