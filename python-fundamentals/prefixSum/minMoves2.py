from math import inf 

def minMoves2(nums):
    nums.sort()
    n = len(nums)
    prefix = [x for x in nums]
    for i in range(1, len(nums)):
        prefix[i] = prefix[i] + prefix[i-1]

    res = inf 

    for i, num in enumerate(nums):

        numMoves = 0
        if i == 0: 
            numMoves += abs(prefix[n-1] - num*(n-1 + 1))
        else: 
            numMoves += abs(prefix[i-1] - num*(i)) 
            numMoves += abs(prefix[n-1] - prefix[i-1] - num*(n-1 - i + 1))
        res = min(numMoves, res)
    return res

nums = [1,10,2,9]
nums = [1,2,3]
nums = [1]
print(minMoves2(nums))