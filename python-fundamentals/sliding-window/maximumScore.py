def maximumScore(nums, k):
    i = j = k
    maxScore = nums[k]
    minNums = nums[k]
    # cycle: move and eval 
    while not( i == 0 and j == len(nums) - 1):
        # go in the dir of the larger num
        if i > 0 and j < len(nums) - 1:
            if nums[i - 1] > nums[j + 1]:
                i -= 1
            else: 
                j += 1
        elif i == 0: 
            j += 1
        elif j == len(nums) - 1:
            i -=1
        minNums = min(minNums, nums[i], nums[j])        
        curScore = minNums*(j - i + 1)
        maxScore = max(maxScore, curScore)        
    return maxScore

nums = [1,4,3,7,4,5]
k = 3

nums = [5,5,4,5,4,1,1,1]
k = 0

print(maximumScore(nums, k))