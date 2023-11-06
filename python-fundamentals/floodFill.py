# floodFill


def floodFill(image, sr, sc, color):
    # plsChange = []
    dirQueue = [(sr, sc)]
    match = image[sr][sc]
    # start with center, then add subsequent cells to iterate over
    # min/max boundaries
    x1 = 0
    x2 = len(image) - 1
    y1 = 0
    y2 = len(image[0]) - 1
    
    visited = {}
    for i in range(len(image)):
        for j in range(len(image[0])):
            visited[(i,j)] = False

    def dequeue(q):
        if len(q) == 0:
            return -1
        res = q[0]
        q = q[1:]
        return (res, q)

    # return adjacent with valids e.g. (1,1) -> (2,1), (0,1), (1,2), (1,0)
    def adjacent(entry, x1, x2, y1, y2):
        (a,b) = entry
        return ([(a + i, b) for i in [-1, 1] if a+i >= x1 and a+i <= x2] + 
                [(a, b + j) for j in [-1,1] if b+j >= y1 and b+j <= y2]) 

    while len(dirQueue) > 0:
        (cur, dirQueue) = dequeue(dirQueue)
        adj = adjacent(cur, x1, x2, y1, y2)
        image[cur[0]][cur[1]] = color
        for x in adj: 
            if not visited[x]:
                visited[x] = True
                if image[x[0]][x[1]] == match:
                    dirQueue.append(x)
    return image


#image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
img = [[1,1,1],[1,1,0],[1,0,1]]
print(floodFill(img, 1, 1, 2))