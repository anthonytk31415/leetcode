def divide(dividend, divisor):
    sign = (dividend >= 0) ^ (divisor >= 0) 
    dividend, divisor, res = [int(x) for x in str(abs(dividend))], abs(divisor), 0
    print(dividend)
    res = 0
    cur = 0
    times = 0
    partialRes = 0
    for i, num in enumerate(dividend): 
        cur += num 
        while partialRes + divisor <= cur: 
            times += 1
            partialRes += divisor
        if times == 0: 
            cur *= 10

        # handle multiplying by 10 and going again
        else: 
            res += times 
            if i < len(dividend) - 1: res *= 10
            cur = 10*(cur - partialRes)
            
        times = 0
        partialRes = 0
    return -res if sign else res 



### you need to solve this using exclusively bits

print(divide(2147483647, 2))

# print(0 & 0)