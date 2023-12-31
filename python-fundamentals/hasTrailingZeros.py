


# def findFirstOne(x):
#     count = 0
#     n = 1
#     while x & (n << count) == 0: 
#         count += 1
#     return count + 1


def hasTrailingZeros(nums):

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            x, y = nums[i], nums[j]
            z = bin(x | y)[-1]
            print(x, y, bin(x|y))
            if z == "0": return True
 
    return False


# nums = [1,2,3,4,5]
# nums = [1,3,5,7,9]
nums = [2,4,8,16]
print(hasTrailingZeros(nums))

# x = 4 & 4

# # print(bin(8 | 4))
# print(8, bin(8))
# print(5, bin(5))


# def trailingTwoZeroes(num):
#     x = bin(num | 4)[2:]
#     print("x:", x)
#     # print(x[-1], x[])
#     # if x[-1] == "0" and x[-2] == 0: return True
#     # else: return False

# print(trailingTwoZeroes(5))