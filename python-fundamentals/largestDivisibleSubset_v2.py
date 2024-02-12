def largestDivisibleSubset(nums):
    nums.sort()
    lengthMultiple = [0]*len(nums)
    parent = [-1]*len(nums)

    for i in range(len(nums)-1, -1, -1):
        curLength = 0
        maxLengthParent = -1

        for j in range(i+1, len(nums)):
            if nums[j] % nums[i] == 0: 
                if lengthMultiple[j] > curLength:
                    curLength = lengthMultiple[j]
                    maxLengthParent = j

        lengthMultiple[i] = curLength + 1
        parent[i] = maxLengthParent

    maxLength = 0
    maxLengthIdx = -1
    for i, n in enumerate(lengthMultiple):
        if maxLength < n: 
            maxLength = n
            maxLengthIdx = i

    res = []
    i = maxLengthIdx
    while i != -1: 
        res.append(nums[i])
        i = parent[i]
    return res

# nums = [1,2,4,8]
nums = [1,2,3]
print(largestDivisibleSubset(nums))