from math import inf 

def maxWidthOfVerticalArea(points):
    points.sort(key = lambda x: x[0])
    prev = points[0][0]
    maxWidth = -inf
    for i in range(1, len(points)):
        cur = points[i][0]
        maxWidth = max(maxWidth, cur - prev)
        prev = cur 
    return maxWidth 

points = [[8,7],[9,9],[7,4],[9,7]]
points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
print(maxWidthOfVerticalArea(points))