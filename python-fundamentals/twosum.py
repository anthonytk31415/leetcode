## twosum


def twoSum(nums, target):
    d = {}
    for i, j in enumerate(nums):
        r = target - j
        if r in d:
            return [d[r], i]
        else:
            d[j] = i


lst = [2,7,11,15]
print(twoSum(lst,9))    
print(list(enumerate(lst)))
