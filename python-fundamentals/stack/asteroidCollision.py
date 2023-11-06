# asteroidCollision

from collections import deque
def asteroidCollision(asteroids):
    pos = deque()
    res = deque()
    curPos, curNeg = None, None
    for x in asteroids: 
        if x > 0: 
            pos.append(x)
        elif x < 0:
            curNeg = x 
            if pos: 
                while pos and curNeg:
                    curPos = pos.pop()
                    if curPos > abs(curNeg):
                        curNeg = None
                        pos.append(curPos)
                        curPos = None
                    elif curPos < abs(curNeg):
                        curPos = None
                    elif curPos == abs(curNeg):
                        curPos = curNeg = None
            if curNeg: 
                res.append(x)
    resPos = deque()
    while pos: 
        resPos.appendleft(pos.pop())
    x = list(res) + list(resPos)
    return x
print(asteroidCollision([5,10,-5]))