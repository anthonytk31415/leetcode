def multiple(num1, num2):
    nums = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    len1 = len(num1)
    len2 = len(num2)
    digits1 = 0
    for x in range(len1):
        y = nums[num1[x]]
        digits1 = digits1 + y * 10 ** (len1 - x-1)
    digits2 = 0
    for x in range(len2):
        y = nums[num2[x]]
        digits2 = digits2 + y * 10 ** (len2 - x-1)
    return str(round(digits1 * digits2))


print(multiple('1212', '345'))


# print(multiple('0', '10'))
