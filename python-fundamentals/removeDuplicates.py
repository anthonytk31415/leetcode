# removeDuplicates

def removeDuplicates(nums):
    if len(nums) <= 1:
        return len(nums)
    i = 0
    z = 0
    end = len(nums) - 1
    while i < end:
        # print(f'i + 1 + z = {i + 1 + z}')
        while i + 1 + z < len(nums) and nums[i] == nums[i+1+z] and (i + 1 +z<= end):
            z += 1
        if z > 0:
            # print(f'z = {z}')
            end -= 1*z
            # print(f'end = {end}')
            # print(f'i: {i}')
            for j in range(i,end+1):
                nums[j] = nums[j+z]
            z = 0
        # print(nums)
        i += 1
    return end + 1

#z = 2, end -=2, 

# a = [1,1,1,2,3]
a = [1,1,1,2,2,2,3,3,4,4,5,5]
# a = [1,1,1]
# a = [1,2]
# a= [1,1]
# a = [1,1,2]
# a = [1,1,1,1,1]

print(removeDuplicates(a))
print(a)



# def removeDuplicates(nums):
    # # print(nums)
    # if len(nums) <= 1:
    #     return len(nums)
    # counter = 0
    # # print(len(nums))
    # i = 0
    # while i < len(nums) - counter:
    #     # print(f'next iteration: {i}, {nums}')
    #     if nums[i] == nums[i+1] and (i + 1 < len(nums)-counter):
    #         # print('range:')
    #         # print(range(i,len(nums)-counter-1))
    #         for j in range(i,len(nums)-counter-1):
    #             nums[j] = nums[j+1]
    #             # print(nums)
    #         counter += 1
    #     else:
    #         i += 1
    # # print(counter)
    # return len(nums)-counter


## not good at handling consecutive dupes
# def removeDuplicates(nums):
#     if len(nums) <= 1:
#         return len(nums)
#     i = 0
#     end = len(nums) - 1
#     while i < end:
#         if nums[i] == nums[i+1] and (i + 1 <= end):
#             for j in range(i,end):
#                 nums[j] = nums[j+1]
#             end -=1
#         else:
#             i += 1
#     return end + 1



def removeDuplicates(nums):
    x = 1
    for i in range(len(nums)-1):
        if nums[i] != nums[i+1]:
            nums[x] = nums[i+1]
            x +=1
    return x