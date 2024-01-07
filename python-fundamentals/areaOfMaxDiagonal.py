from math import inf, sqrt
def areaOfMaxDiagonal(dimensions):
    dim = dimensions
    maxArea = -inf
    maxDiag = -inf
    for a, b in dim: 
        diag = sqrt(a**2 + b**2)
        if diag > maxDiag: 
            maxDiag = diag
            maxArea = a*b
        if diag == maxDiag: 
            maxArea = max(maxArea, a*b)

    return maxArea

dimensions = [[9,3],[8,6]]
dimensions = [[3,4],[4,3]]
dimensions = [[2,6],[5,1],[3,10],[8,4]]
dimensions = [[6,5],[8,6],[2,10],[8,1],[9,2],[3,5],[3,5]]
print(areaOfMaxDiagonal(dimensions))