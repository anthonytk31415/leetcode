# sort colors (counting sort?)

def sortColors(nums):
    c = [0,0,0]
    b = [0 for x in nums]
    for j in range(len(nums)):
        c[nums[j]] = c[nums[j]] + 1
    # now c contains the number of elements equal to i
    for i in range(1,len(c)):
        c[i] = c[i] + c[i-1]
    # now c contains num of elements <= i
    print(c)
    for j in range(len(nums)-1, -1, -1):
        # print(j)
        b[c[nums[j]]-1] = nums[j]
        c[nums[j]] = c[nums[j]] - 1 # decrement by one to handle dupes
        # print(b)
        # print(c)
    for i in range(len(nums)):
        nums[i] = b[i]
    

a = [2,0,2,1,1,0]

print(sortColors(a))