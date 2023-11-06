from heapq import heappush, heappop

# k log k time, n space

def kthSmallest(matrix, k):
    visited = set()
    visited.add((0,0))
    queue = [(matrix[0][0], (0,0))]
    e = 0
    while e < k: 
        val, coords = heappop(queue)
        (i,j) = coords
        e +=1
        for (u,v) in [(i +1, j), (i, j+1)]:
            if 0 <= u < len(matrix) and 0 <= v < len(matrix[0]) and (u,v) not in visited: 
                visited.add((u,v))
                heappush(queue, (matrix[u][v], (u, v)))
    return val

matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
print(kthSmallest(matrix, k))