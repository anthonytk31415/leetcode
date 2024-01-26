# 600. Non-negative Integers without Consecutive Ones


# x = 0 & 0 
# print(bin(x))

# x = 3 & 11
# print(bin(x))


# linear n TLE
def findIntegers(n):
    res = 0
    for x in range(3, n+1):
        y = x
        while y >= 3: 
            if y & 3 == 3: 
                res += 1
                break
            y = y >> 1
    return  n + 1 - res 

print(findIntegers(100000000))
# print(bin(x))
