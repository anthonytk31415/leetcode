def minMovesToCaptureTheQueen(a,b,c,d,e,f):
    rook = (a,b)            # a, b = row a, col b
    bishop = (c,d)
    queen = (e,f)

    rookInWay = False
    i, j = e, f
    i +=1
    j += 1
    while i < 9 and j < 9: 
        if (i, j) == rook: rookInWay = True
        if (i,j) == bishop: 
            if rookInWay: return 2
            else: return 1
        i +=1
        j +=1

    rookInWay = False
    i, j = e, f
    i -=1
    j -= 1
    while i >0 and j >0: 
        if (i, j) == rook: rookInWay = True
        if (i,j) == bishop: 
            if rookInWay: return 2
            else: return 1
        i -=1
        j -= 1

    rookInWay = False
    i, j = e, f
    i -=1
    j +=1
    while i > 0 and j < 9: 
        if (i, j) == rook: rookInWay = True
        if (i,j) == bishop: 
            if rookInWay: return 2
            else: return 1
        i -=1
        j +=1

    rookInWay = False
    i, j = e, f
    i +=1
    j -=1
    while i < 9 and j >0: 
        if (i, j) == rook: rookInWay = True
        if (i,j) == bishop: 
            if rookInWay: return 2
            else: return 1
        i +=1
        j -=1

    # rook
    if a == e: 
        if b > f: x, y = f, b
        else: x, y = b, f
        if c == a and x < d < y: return 2
        else: return 1
    if b == f:  
        if a > e: x, y = e, a
        else: x, y = a, e
        if d == b and x < c < y: return 2
        else: return 1

    return 2

# a = 1
# b = 1 
# c = 8 
# d = 8 
# e = 2 
# f = 3
# -1 for now; later, 2

# a = 2
# b = 1 
# c = 2 
# d = 2 
# e = 2 
# f = 3
# 2

# a = 1
# b = 3 
# c = 8 
# d = 3 
# e = 7 
# f = 3
# 1

# bishiop direct attacking queen
a = 2
b = 7 
c = 4
d = 7 
e = 3 
f = 8


print(minMovesToCaptureTheQueen(a,b,c,d,e,f))