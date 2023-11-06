def moveZeroes(nums):
    j = None
    i = 0
    while i < len(nums):
        if nums[i] != 0 and j == None: 
            i +=1
            continue
        elif nums[i] !=0 and j != None and j < i: 
            nums[i], nums[j] = nums[j], nums[i]
            j +=1

        elif nums[i] == 0 and j == None: 
            j = i
        elif nums[i] == 0 and j != None: 
            i +=1
            continue
        i +=1

# def moveZeroes(nums):
#     j = None
#     i = 0
#     while i < len(nums):
#         if nums[i] == 0: 
#             j = i
#             break 
#         i +=1
    
#     if j == None:



nums = [0,1,0,3,12]
moveZeroes(nums)
print(nums)


# ** everything < 0 is all non zero ** 
# ** everything bewteen j and i for j <= i is a  zero
# if not zero and zero occurred before: swap 
#     j +=1

# if not zero and no zero occurred before: continue
# if zero and no j: j = i
# if zero and j: continue


# 0 1 0 3 0 1 2;  i = 0; j = 0
# 1 0 0 3 0 1 2;  i = 1; then j = 1
# 1 0 0 3 0 1 2;  i = 2;
# 1 3 0 0 0 1 2;  i = 3; then j = 2 
# 1 3 1 0 0 0 2
# 1 3 1 2 0 0 0 

