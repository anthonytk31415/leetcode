def removeElement(nums, val):
    counter = 0 
    i = 0
    while i < len(nums) - counter:
        print(nums, counter, i)
        if nums[i] == val: 
            for j in range(i, len(nums) - counter - 1): 
                nums[j] = nums[j+1]

            counter +=1
        else: 
            i += 1
    return len(nums) - counter

# 7, 3, 
a = [0,1,1,2,2,1,3]    
print(removeElement(a, 1))
print(a)


#, 1
# [0,2,1]

# The New Dehli Power Rangers
