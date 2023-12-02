def binaryGap(n):
    maxGap = 0
    # move past the first one 

    print(bin(n))
    while n > 0 and n & 1 == 0: 
        n = n >> 1
    n = n >> 1
    if n == 0: 
        return maxGap
    gap = 1
    while n > 0:
        if n & 1 == 1: 
            maxGap = max(maxGap, gap)
            gap = 0
        n = n >> 1
        gap += 1

    return maxGap

# n = 8

# when you zip unequal things, itll take the smallest length of the zips
n = 76
zipped = zip(bin(n)[2:], bin(n)[3:], bin(n)[4:])
print(list(zipped))
print("res: ", binaryGap(n))

