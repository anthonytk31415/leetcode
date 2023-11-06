#1d Array

# def runningSum(lst):
#     return list(sum(lst[0:(x+1)]) for x in range(len(lst)))


def runningSum(nums):
    res = []
    holder = 0
    for i in nums:
        holder = holder + i
        res.append(holder)
    return res



lst = [1,3,5,7]
print(runningSum(lst))

