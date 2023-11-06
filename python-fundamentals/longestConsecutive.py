# longestConsecutive


# def longestConsecutive(nums):
    # if len(nums) <=1:
    #     return len(nums)   
    # numMin = min(nums)
    # ## let the min start at 0
    # nums = [x - numMin for x in nums]
    # numMin = numMin - numMin # ensure this starts at 0
    # # print(numMin)
    # numMax = max(nums)
    # c = [0 for x in range(numMax+1)]
    # for x in nums:
    #     c[x] +=1 
    # # print(c)
    # # ensure that counting is appropriate
    # curMax = 0
    # counter = 0
    # for i in range(len(c)):
    #     # print(c[i])
    #     if c[i] == 0:
    #         curMax = max(curMax, counter)
    #         counter = 0
    #     else: 
    #         counter += 1
    #     curMax = max(curMax, counter)
    # return curMax



def longestConsecutive(nums):
# the concept is for each num in the list of numbers, check if there's a consecutive one (x + 1, x - 1)
# if so, with a dictionary, mark as 'checked' and then check if new x+1 ; then do that process with x-1
    if len(nums) <= 0:
        return len(nums)
    nums = set(nums)
    visited = dict([(x, False) for x in nums])    
    curLength = 1
    maxLength = 1
    for x in nums:
        if visited[x]: 
            continue
        else: 
            visited[x] = True
            #traverse upper consecutive 
            y = x - 1
            while y in visited and visited[y] == False:
                visited[y] = True
                curLength +=1
                y = y - 1
            #traverse lower consecutive
            # z = x - 1
            # do this on x so you mark these x values false for speed
            while x+1 in visited and visited[x+1]==False:
                visited[x+1] = True
                curLength += 1
                x = x + 1
        maxLength = max(maxLength, curLength)
        # reset conditions for the next num
        curLength = 1            
    return maxLength

    


# 0 > 0,1,2,3 > x
# 3 > 2,3 > x
# 7 > 7,8 > x
# 5 > 4,5 > 4,5,6,7,8 > 0,1,2,3,4,5,6,7,8 

nums = [0,3,7,2,5,8,4,6,0,1] # 
# nums = [1,4,0, 9]
print(longestConsecutive(nums))

# print(longestConsecutive([-5, 0, 1, 3, -6, 9, -4, 11, -3]))

## this makes the algo above too long
# nums = [0,1,2,4,8,5,6,7,9,3,55,88,77,99,999999999]

