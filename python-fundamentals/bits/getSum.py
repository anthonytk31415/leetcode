from collections import deque
# this only works for positive digits a and b
def getSum(a, b):
    res = deque()

    a = deque(list(int(x) for x in bin(a)[2:]))
    b = deque(list(int(x) for x in bin(b)[2:]))
    curC = 0       
    nextC = 0
    while a and b: 
        curA = a.pop()
        curB = b.pop()
        
        curDigit = (curA ^ curB) ^ curC
        nextC = (curA & curB) | ((curA | curB) & curC)            

        res.appendleft(curDigit)
        curC, nextC = nextC, 0

    while a: 
        curA = a.pop()
        curDigit = curA ^ curC 
        nextC = curA & curC 
        res.appendleft(curDigit)
        curC, nextC = nextC, 0

    while b: 
        curB = b.pop()
        curDigit = curB ^ curC 
        nextC = curB & curC 
        res.appendleft(curDigit)
        curC, nextC = nextC, 0

    resInt = 0
    twoPlace = 0
    while res: 
        cur = res.pop()
        resInt += 2** twoPlace * cur
        twoPlace += 1

    return resInt

a = 12338
b = 238

for x in [a, b]:
    print(bin(x))

print(getSum(a, b))



# how should i handle negatiev numbers? 


