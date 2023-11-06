from math import sqrt

def checkOverlap(radius, xCenter, yCenter, x1, y1, x2, y2):
    
    a, b = (x1 + x2)/2, (y1 + y2)/2

    ## check vertices inside circle 
    for u, v in [(x1, y1),(x1, y2), (x2, y1) , (x2, y2), (a, b)]:
        if sqrt((u - xCenter)**2 + (v - yCenter)**2 ) <= radius: 
            return True

    ## check poles inside rectangle
    for u, v in [(xCenter + radius, yCenter), (xCenter - radius, yCenter), (xCenter, yCenter + radius), (xCenter, yCenter - radius)]:
        if x1 <= u <= x2 and y1 <= v <= y2: 
            return True

    if xCenter - radius <= x1 <= x2 <= xCenter + radius: 
        if (y1 <= yCenter - radius <= yCenter + radius <= y2) or (yCenter - radius <= y1 <= y2 <= yCenter + radius): 

            return True

    if yCenter - radius <= y1 <= y2 <= yCenter + radius: 
        if (x1 <= xCenter - radius <= xCenter + radius <= x2) or (xCenter - radius <= x1 <= x2 <= xCenter + radius):
            return True

    return False

# radius = 1
# xCenter = 0
# yCenter = 0
# x1 = 1
# y1 = -1
# x2 = 3
# y2 = 1

# radius = 1
# xCenter = 1
# yCenter = 1
# x1 = 1
# y1 = -3
# x2 = 2
# y2 = -1

# radius = 1206
# xCenter = -5597
# yCenter = -276
# x1 = -5203
# y1 = -1795
# x2 = -4648
# y2 = 1721


radius = 3
xCenter = 0
yCenter = 0
x1 = -4
y1 = 1
x2 = 10000
y2 = 2

# radius = 4
# xCenter = 9
# yCenter = 3
# x1 = 1
# y1 = 5
# x2 = 2
# y2 = 10


print(checkOverlap(radius, xCenter, yCenter, x1, y1, x2, y2))


# radius = 1, xCenter = 1, yCenter = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1