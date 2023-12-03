from math import sqrt



# a = (-5, -6)
# b = (-2, -3)

# # a = (-2, -4)
# # b = (7, 13)

# print(minRoute(a, b))


def minTimeToVisitAllPoints(points):
    def chebychev(a, b):
        (x0, y0) = a
        (x1, y1) = b
        return max(abs(x0 - x1), abs(y0 - y1))

    res = 0
    for i in range(1, len(points)):
        res += chebychev(points[i-1], points[i])
    return res


points = [[1,1],[3,4],[-1,0]]

print(minTimeToVisitAllPoints(points))