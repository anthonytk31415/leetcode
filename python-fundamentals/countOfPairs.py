def countOfPairs(n, x, y):
    def dist(a,b): 
        return abs(b - a)
    res = [0]*n
    
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            k = min(dist(i, j), dist(i, x) + dist(y, j) + 1, dist(i, y) + dist(x, j) + 1)
            res[k-1] += 2
    return res

n = 5
x = 2
y = 4

n = 4
x = 1
y = 1

n = 3
x = 3
y = 1

print(countOfPairs(n, x, y))