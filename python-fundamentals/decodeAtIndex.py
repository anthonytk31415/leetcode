def seperateStringAndInteger(chars):
    res = []
    curString = ""
    charLength = 0
    for x in chars:
        if x.isnumeric(): 
            if curString != "":
                charLength += len(curString)
                res.append(curString)
                curString = ""
            res.append(int(x))
            charLength *= int(x)
        else: 
            curString = curString + x
    if curString != "": 
        charLength += len(curString)
        res.append(curString)
        curString = ""
    return (res, charLength)

def decodeAtIndex(s, k):

    k = k - 1

    def seperateStringAndInteger(chars):
        res = []
        curString = ""
        charLength = 0
        for x in chars:
            if x.isnumeric(): 
                if curString != "":
                    charLength += len(curString)
                    res.append(curString)
                    curString = ""
                res.append(int(x))
                charLength *= int(x)
            else: 
                curString = curString + x
        if curString != "": 
            charLength += len(curString)
            res.append(curString)
            curString = ""
        return (res, int(charLength))

    stack, charLength = seperateStringAndInteger(s)
    while stack: 
        top = stack.pop()
        if isinstance(top, int): 
            charLength //= top
            k = int(k % charLength)
        else: 
            if charLength - len(top)  <= k <= charLength - 1:                
                return top[(k - charLength)]
            else: 
                charLength -= len(top)
    return -1

# s = "leet2code3"
# k = 10

s = "a2345678999999999999999"
k = 1

# s = "ha229192"
# k = 2

print(decodeAtIndex(s, k))


# a = "1"
# print(a.isnumeric())


# a = 2*3*4*5*6*7*8*9*9*9*9*9*9*9*9*9*9*9*9*9*9*9
# print(a%1)