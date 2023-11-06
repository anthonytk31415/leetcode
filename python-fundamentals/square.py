

from math import sqrt

def dist(a,b): 
    (x1,y1) = a
    (x2,y2) = b
    return sqrt( (x1 - x2)**2 + (y1 - y2)**2)


a = [(-6,-6),
(-3, -3),
(-3, -8),
(-1,-5)]

a.sort()

print(a)