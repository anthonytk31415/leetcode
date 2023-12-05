# def rangeBitwiseAnd(left, right):
#     if left == right: 
#         return left 

#     leftBL = left.bit_length()
#     rightBL = right.bit_length()

#     for n in [leftBL - 1, leftBL, rightBL-1, rightBL]:
#         if left < 2**n < right: 
#             return 0

#     bitsToAdd = 0
#     endings = [left, right]
#     for y in [endings[0], endings[1]]:
#         bitLength = (y & -y).bit_length()
#         bitsToAdd += bitLength - 1
#         for i, x in enumerate([endings[0], endings[1]]):
#             endings[i] = endings[i] >> (bitLength - 1)

#     endings[0] = endings[0] & endings[1]
#     cur = endings[0]

#     while cur + 1 <= endings[1]: 
#         cur &= cur + 1
#         cur += 1
#         bitLength = (cur & -cur).bit_length()
#         bitsToAdd += bitLength - 1
#         for i, x in enumerate([left, right]):
#             endings[i] = endings[i] >> (bitLength - 1)
#     if cur == 0: 
#         return cur
#     return cur << bitsToAdd 


def rangeBitwiseAnd1(left, right):
    leftBL = left.bit_length()
    rightBL = right.bit_length()

    for n in [leftBL - 1, leftBL, rightBL-1, rightBL]:
        if left < 2**n < right: 
            return 0

    res = left
    cur = left + 1
    while cur <= right: 
        res &= cur
        cur += 1
    return res


def rangeBitwiseAnd(left, right):

    alpha = left | (left & -left) 
    cur = left
    while True: 
        right = left & right
    return right



# left = 600000000
# right = 2147483645

# 1073741824
# left  = 1073741824
# right = 2147483647
# left = 100



# left = 1
# right = 2147483647

# left = 0
# right = 0


left = 10
right = 7

# print(left & right)
# print(5&6)
# print(6&7)
# # x & y <= min(x, y)
# print(18 & 12)

# print(5 & 38 & 8)
# print(bin(15))


# print(9&10)
# print(10&11&12&13&14)
# print(bin(10))

# print("left: ", bin(left))
# newShift = (left & -left).bit_length() - 2
# alphaPlus = left + (2 << newShift)
# print(bin(left & alphaPlus))

# alpha = left | (left & -left)
# print(bin(alpha))

# print("fn0 call: ", rangeBitwiseAnd(left, right))
# print("fn1 call: ", rangeBitwiseAnd1(left, right))


def crudeOps(a, b):
    cur = a
    for i in range(a + 1, b + 1): 
        cur = cur & i
    return cur


def crudeOps1(a, b):

    if a == b: 
        return a 

    leftBL = a.bit_length()
    rightBL = b.bit_length()

    for n in [leftBL - 1, leftBL, rightBL-1, rightBL]:
        if left < 2**n < right: 
            return 0

    n = (a & -a).bit_length() - 1
    print(n, bin(a))
    cur = a
    while cur + 2**n < b:  
        cur = int(cur & (cur + 2**n))
        n += 1
        if cur == 2**(a.bit_length() - 1): 
            break 
    return cur & b
    # start adding 
# print(crudeOps(101, 126))
# print(crudeOps1(101, 126))

# left  = 1073741824
# right = 2147483647

left = 5
right = 12

# print(5&6&7&8)

print(crudeOps(left, right))
print(crudeOps1(left, right))



# print(crudeOps(13, 15))
# print(13&14&15)
# print(crudeOps(11,15))