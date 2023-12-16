from math import inf 

def maxDistToClosest(seats):
    seats = seats 
    left = -1
    maxGap = 0
    for right, seat in enumerate(seats):
        if seat == 1: 
            if left == -1: maxGap = max(maxGap, right)
            else: maxGap = max(maxGap, (right - left)//2)
            left = right
    maxGap = max(maxGap, (len(seats) - 1 - left))
    return maxGap

s0 = [1,0,0,0,1,0,1] # 2
s1 = [0,0,0,1] # 3
s2 = [1,0,0,0] # 3
s4 = [0,0,1,0,0,1,0,1]
for x in [s0, s1, s2, s4]:
    print(maxDistToClosest(x))