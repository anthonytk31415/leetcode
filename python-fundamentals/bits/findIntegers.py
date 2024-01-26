# 600. Non-negative Integers without Consecutive Ones


# x = 0 & 0 
# print(bin(x))

# x = 3 & 11
# print(bin(x))


#  TLE
# O(n *k)
def findIntegers1(n):
    res = 0
    for x in range(3, n+1):
        y = x
        while y >= 3: 
            if y & 3 == 3: 
                res += 1
                break
            y = y >> 1
    return  n + 1 - res 

# this is O(n); too slow
def findIntegers(n):
    res = 0
    for x in range(3, n+1):
        if (x & (x << 1) > 0): res += 1
    return  n + 1 - res 


#  1010
# 10100

#  10000110
# 100001100

print(findIntegers(100000000))
# print(bin(x))
