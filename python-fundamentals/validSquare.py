from math import sqrt


def validSquare1(p1, p2, p3, p4):

    def distance(p1, p2):
        x0, y0 = p1
        x1, y1 = p2
        return sqrt((x1 - x0)**2 + (y1 - y0) **2)
    points = [p1, p2, p3, p4]
    points.sort()
    [p1, p2, p3, p4] = points
    print(points)
    dist = distance(p1, p2)
    if dist != int(dist): 
        return False
    dist = int(dist)
    x,y = p1
    if [x, y + dist] == p2 and [x + dist, y] == p3 and [x + dist, y + dist] == p4:
        return True

    return False
    # print(points)

from collections import defaultdict

def validSquare(p1, p2, p3, p4):
    points = [p1, p2, p3, p4]
    pointSet = set([tuple(x) for x in points])
    if len(pointSet) != 4:
        return False 

    def distanceSquared(p1, p2):
        x0, y0 = p1
        x1, y1 = p2
        return ((x1 - x0)**2 + (y1 - y0) **2)


    distances = defaultdict(int)
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            u = points[i]
            v = points[j]
            dist_sq = distanceSquared(u, v)
            distances[dist_sq] +=1
    
    if len(distances.keys()) == 2:
        a, b = distances.keys()
        if (distances[a] == 2 and distances[b] == 4) or (distances[a] == 4 and distances[b] == 2):
            return True

    return False



# p1 = [0,0] 
# p2 = [1,1] 
# p3 = [1,0]
# p4 = [0,1]

# p1 = [1,0] 
# p2 = [-1,0] 
# p3 = [0,1]
# p4 = [0,-1]


# print(validSquare(p1, p2, p3, p4))


p1 = [0,0] 
p2 = [1,1] 
p3 = [1,0]
p4 = [0,12]

print(validSquare(p1, p2, p3, p4))