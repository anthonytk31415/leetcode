# Time: O(2**n)
# Space: O(2**n)

def subsets(nums):

    res = [[]]
    if not nums: 
        return res
    for x in nums: 
        res = res + [y + [x] for y in res]
    return res



nums = [1,2,3]

print(subsets(nums))


# if 
# [] => [[]]
# 1: [[]], [[1]]
# 2 : [[]]], [[1]], -->  [[2]]], [[1, 2]]
# 3 : [[]]], [[1]], [[2]]], [[1, 2]] --> [[3]]], [[1, 3]], [[2, 3]]], [[1, 2, 3]]
