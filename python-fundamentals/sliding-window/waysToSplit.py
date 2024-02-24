def waysToSplit(nums):


    def sumNums(start, end):
        if start == 0: 
            return prefix[end]
        return prefix[end] - prefix[start - 1]


    prefix = [x for x in nums]
    for i in range(1, len(prefix)):
        prefix[i] = prefix[i] + prefix[i + 1]
    
    res = 0
    minLeft = 1
    maxLeft = 1
    for right in range(2, len(prefix)):
        rightSum = sumNums(right, len(prefix) - 1)
        while maxLeft +1 < right - 1 and sumNums(0, maxLeft ) <= sumNums(maxLeft+1, right - 1) <= rightSum:
            maxLeft += 1
        while minLeft - 1 > 1 and sumNums(0, minLeft - 1 - 1) <= sumNums(minLeft-1, right - 1) <= rightSum:
            minLeft -= 1

        if 
            res += maxLeft - minLeft + 1
    return res % (10**9 + 7)


# nums = [1,1,1]
nums = [1,2,2,2,5,0]

print(waysToSplit(nums))