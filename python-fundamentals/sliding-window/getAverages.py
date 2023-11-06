def getAverages(nums, k):

    start = 0
    end = 2*k 
    i = k
    res = [-1 for _ in range(len(nums))]
    window = sum(nums[start:end + 1])
    denom = 2*k + 1

    while end < len(nums):
        curAvg = (window // denom)
        res[i] = curAvg
        window -= nums[start]
        start +=1
        end += 1        
        i += 1
        if end < len(nums):            
            window += nums[end]

    return res


nums = [7,4,3,9,1,8,5,2,6]
k = 3
print(11//4)
print(35//7)


print(getAverages(nums, k))