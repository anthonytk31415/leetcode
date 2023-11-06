# Simple O(n) run time with O(n) space
def findDisappearedNumbers(nums):
    a = set(nums)
    res = []
    for i in range(1, len(nums)+1):
        if i not in a: 
            res.append(i)

    return res



# can we write this with no extra space? 
# this is still Time = O(n), space = constant (not incliuding the result)
def findDisappearedNumbers(nums):
    res = set([i for i in range(1, len(nums)+1)])
    for x in nums: 
        if x in res: 
            res.remove(x)
    return list(res)