def knightProbability(n, k, row, column):
    
    dpPrev = [[1 for _ in range(n)] for _ in range(n)]
    dpCur = [[0 for _ in range(n)] for _ in range(n)]

    for _ in range(k):
        for i in range(n):
            for j in range(n):
                print(i,j)
                curRes = 0
                for uDelta, vDelta in [(1,2), (2,1), (-1,2), (-2,1), (1,-2), (2,-1), (-1,-2), (-2,-1)]:
                    u, v = i + uDelta, j + vDelta
                    if 0 <= u < n and 0 <= v < n: 
                        curRes += dpPrev[u][v]*1/8
                dpCur[i][j] = curRes
    
        dpPrev, dpCur = dpCur, [[0 for _ in range(n)] for _ in range(n)]

    return dpPrev[row][column]

n = 3 
k = 2
row = 0
column = 0

n = 1
k = 0
row = 0
column = 0

print(knightProbability(n, k, row, column))