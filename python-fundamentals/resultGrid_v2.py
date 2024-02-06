
from math import floor

def resultGrid(image, threshold):

    def testRegion(i, j): 
        adjacents = [
            ((i, j), (i +1, j)),
            ((i, j+1), (i+1, j+1)),
            ((i, j+2), (i+1, j+2)),
            ((i+1, j), (i+2, j)),
            ((i+1, j+1), (i+2, j+1)),
            ((i+1, j+2), (i+2, j+2)),

            ((i, j), (i, j+1)),
            ((i+1, j), (i+1, j+1)),
            ((i+2, j), (i+2, j+1)),
            ((i, j+1), (i, j+2)),
            ((i+1, j+1), (i+1, j+2)),
            ((i+2, j+1), (i+2, j+2)),
        ]

        for u, v in adjacents:
            a, b = u
            c, d = v
            if abs(image[a][b] - image[c][d]) <= threshold: continue
            else: return False
        return True

    def avgIntensity(i, j):
        indexChecks =  [ (i, j), (i, j+1), (i, j+2), 
                        (i+1, j), (i+1, j+1), (i+1, j+2), 
                        (i+2, j), (i+2, j+1), (i+2, j+2)]

        res = 0
        for u, v in indexChecks: 
            res += image[u][v]            
        return floor(res/9)

    def addRegionIntensityToRes(i, j):
        indexChecks =  [ (i, j), (i, j+1), (i, j+2), 
                (i+1, j), (i+1, j+1), (i+1, j+2), 
                (i+2, j), (i+2, j+1), (i+2, j+2)]

        for u, v in indexChecks: 
            res[u][v] += regions[(i, j)]
            countRegions[u][v] += 1
        
        return


    regions = {}

    for i in range(len(image) - 2):
        for j in range(len(image[0]) - 2):
            if testRegion(i,j):
                regions[(i, j)] = avgIntensity(i, j)

    print(regions)

    res = [[0 for _ in range(len(image[0]))] for _ in range(len(image))]
    countRegions = [[0 for _ in range(len(image[0]))] for _ in range(len(image))]

    for i, j in regions.keys():
        addRegionIntensityToRes(i, j)

    superRes = [[0 for _ in range(len(image[0]))] for _ in range(len(image))]

    for i in range(len(image)):
        for j in range(len(image[0])):
            check = countRegions[i][j] 
            if check > 0: superRes[i][j] = floor(res[i][j]/countRegions[i][j])
            elif check == 0: superRes[i][j] = image[i][j]

    return superRes
    
image = [[10,20,30],[15,25,35],[20,30,40],[25,35,45]]
threshold = 12


# image = [[5,6,7],[8,9,10],[11,12,13]]
# threshold = 1
image = [[0,0,0,0,0,0,1,0,0,0,0,7,0,4,0,0,0,7,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,0,0,0,0,7,0,4,0,0,0,7,0,0,0,0,0,0,0],
        [4,4,4,4,4,4,5,4,4,4,4,11,4,8,4,4,4,11,4,4,4,4,4,4,4],
        [0,0,0,0,0,0,1,0,0,0,0,7,0,4,0,0,0,7,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,0,0,0,0,7,0,4,0,0,0,7,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,0,0,0,0,7,0,4,0,0,0,7,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,0,0,0,0,7,0,4,0,0,0,7,0,0,0,0,0,0,0],
        [4,4,4,4,4,4,5,4,4,4,4,11,4,8,4,4,4,11,4,4,4,4,4,4,4],
        [9,9,9,9,9,9,10,9,9,9,9,16,9,13,9,9,9,16,9,9,9,9,9,9,9],
        [0,0,0,0,0,0,1,0,0,0,0,7,0,4,0,0,0,7,0,0,0,0,0,0,0],
        [5,5,5,5,5,5,6,5,5,5,5,12,5,9,5,5,5,12,5,5,5,5,5,5,5],
        [16,16,16,16,16,16,17,16,16,16,16,23,16,20,16,16,16,23,16,16,16,16,16,16,16],
        [0,0,0,0,0,0,1,0,0,0,0,7,0,4,0,0,0,7,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,0,0,0,0,7,0,4,0,0,0,7,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,0,0,0,0,7,0,4,0,0,0,7,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,0,0,0,0,7,0,4,0,0,0,7,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,0,0,0,0,7,0,4,0,0,0,7,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,0,0,0,0,7,0,4,0,0,0,7,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,0,0,0,0,7,0,4,0,0,0,7,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,0,0,0,0,7,0,4,0,0,0,7,0,0,0,0,0,0,0],
        [8,8,8,8,8,8,9,8,8,8,8,15,8,12,8,8,8,15,8,8,8,8,8,8,8],
        [0,0,0,0,0,0,1,0,0,0,0,7,0,4,0,0,0,7,0,0,0,0,0,0,0],
        [1,1,1,1,1,1,2,1,1,1,1,8,1,5,1,1,1,8,1,1,1,1,1,1,1],
        [0,0,0,0,0,0,1,0,0,0,0,7,0,4,0,0,0,7,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,0,0,0,0,7,0,4,0,0,0,7,0,0,0,0,0,0,0]]
threshold = 41

print(resultGrid(image, threshold))

print(6 //9)