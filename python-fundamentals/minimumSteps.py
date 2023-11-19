from functools import lru_cache

@lru_cache()
def minimumSteps1(s):
    if len(s) == 0: 
        return 0
    # if the last element is 1, then call the fucntion again on minimuSteps(s[:-1])
    if s[-1] == "1": 
        return minimumSteps(s[:-1])
    #else: 
    # count how many 0's you see until you get to a 1, then return x + minimumSteps(s[:-x])

    countZeroes = 0
    findOne = False
    i = len(s) - 1
    while i > 0: 
        if s[i] == "0":
            countZeroes += 1
            i -=1
        if s[i] == "1":
            findOne = True
            break
 
    if findOne: 
        newStr = s[:i]+ "0" * countZeroes
        return countZeroes + minimumSteps(newStr) 
    else: 
        return 0


def minimumSteps(s):
    res = 0
    countZeroes = 0
    for i in range(len(s)-1, -1, -1):
        curNum = s[i]
        if curNum == "0": 
            countZeroes += 1
        else: 
            res += countZeroes
    return res

# s = "1010110101101011010110101101011010110101101011010110101101011010110101101011010110101101011010110101101011010110101101011010110101101011010110101101011010110101101011010110101101011010110101101011010110101101011010110101101011010110101101011010110101101011010110101101011010110101101011010110101101011010110101101011010110101101011010110101101011010110101101011010110101101011010110101101011010110101101011010110101101011010110101101011010110101101011010110101101011010110101101011010110101101011010110101101011010110101101011010110101101011010110101101011010110101101011010110101101011010110101101011010110101101011010110101101011010110101101011010110101101011010110101101011010110101101011010110101"

# s = "101010101010"
s = "100100"
# # s[:0]
# print(s[:0])
print(minimumSteps(s))