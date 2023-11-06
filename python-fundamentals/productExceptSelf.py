# productExceptSelf


## lets first use two arrays and then we can do some fancy calcs to just maintain one
# def productExceptSelf(nums):
#     left = [1] * len(nums)
#     right = [1] * len(nums)
#     for i in range(1, len(nums)):
#         left[i] = left[i-1]*nums[i-1]
#     for i in range(len(nums)-2, -1, -1):
#         right[i] = right[i+1]*nums[i+1]
#     return [x[0]*x[1] for x in zip(left, right)]


# the trick is you go right first and then go left on the array
# notice that res[i] = left[i] * right[i] where left[i] and right[i] are the products of the
# numbers on the respective sides
# note that i increaess, you just take the result of the prior * the new number. For example, 
# going left: i = 0: left = 1; i in range(len(nums)): left[i] = left[i-1]*nums[i]. Note the cumulative sum.
# then going right: i = N: right = 1; i in range(len(nums)-2, -1, -1) right[i] = right[i+1] * nums[i+1]
# the result = left[i] * right[i] for i in range(len(nums)) 
# you can do fancy algebra and remove the "right" array by first doing left, then keeping a cumulative product: 
# rCum = rCum[i+1] * nums[i+1] as you roll down
#  
def productExceptSelf(nums):
    res = [1] * len(nums)
    for i in range(1, len(nums)):
        res[i] = res[i-1]*nums[i-1]
    rCum = 1
    for i in range(len(nums)-2, -1, -1):
        rCum = rCum * nums[i+1]
        res[i] = res[i] * rCum
    return res


arr = [1,2,3,4]
print(productExceptSelf(arr))