def maxStrength(nums):
    pos = None
    neg = None 
    largestNeg = None
    zero = None
    for num in nums: 
        if num > 0: 
            if pos == None: pos = num
            else: pos *= num
        if num < 0: 
            if neg == None: 
                largestNeg = num
                neg = num
            else: 
                largestNeg = max(largestNeg, num)
                neg *= num            
        if num == 0: 
            zero = 0
    print(pos, neg, largestNeg, zero)


    if pos != None:
        if neg != None: 
            if neg > 0: return pos * neg
            if neg < 0: return int(pos * neg / largestNeg)
        else: 
            return pos
    else: 
        if neg == None: return 0
        if neg > 0: return neg
        if neg != None and neg != largestNeg: return int(neg / largestNeg)
        elif zero != None: return 0
        else: return largestNeg


nums = [-4,-5,-4]
nums = [3,-1,-5,2,5,-9]
nums = [0, -1]

nums = [-1, -10, -5]
nums = [-4, -3]
nums = [0]
# nums = [0, 1]
print(maxStrength(nums))
