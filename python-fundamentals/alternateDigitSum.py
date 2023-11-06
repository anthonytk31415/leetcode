def alternateDigitSum(n):
    res = 0
    sign = 1
    for x in str(n):
        res += sign*int(x)
        sign *= -1 
    return res


print(alternateDigitSum(521))