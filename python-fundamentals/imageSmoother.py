from math import floor
def imageSmoother(img):

    def cellSmoother(i, j):
        neighbors = []
        for u, v in [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]:
            if 0 <= u < len(img) and 0 <= v < len(img[0]):
                neighbors.append(img[u][v])
        return floor(sum(neighbors) / len(neighbors))


    res = [[0 for _ in img[0]] for _ in img ]
    for i in range(len(img)):
        for j in range(len(img[0])):
            res[i][j] = cellSmoother(i, j)
    
    return res

img = [[100,200,100],[200,50,200],[100,200,100]]
print(imageSmoother(img))