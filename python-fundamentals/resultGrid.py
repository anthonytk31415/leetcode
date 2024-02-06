
from math import floor


    

def resultGrid(image, threshold):

    def cell1Check(i, j):
        for (u,v) in [(i+1, j), (i, j+1)]:
            if 0 <= u < len(image) and 0 <= v < len(image[0]) and abs(image[i][j] - image[u][v]) <= threshold: continue
            else: 
                return False 
        return True

    def cell2Check(i, j):
        for (u,v) in [(i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= u < len(image) and 0 <= v < len(image[0]) and abs(image[i][j] - image[u][v]) <= threshold: continue
            else: 
                return False 
        return True
    def cell3Check(i, j):
        for (u,v) in [(i+1, j), (i, j-1)]:
            if 0 <= u < len(image) and 0 <= v < len(image[0]) and abs(image[i][j] - image[u][v]) <= threshold: continue
            else: 
                return False 
        return True
    def cell4Check(i, j):
        for (u,v) in [(i-1, j), (i+1, j), (i, j+1)]:
            if 0 <= u < len(image) and 0 <= v < len(image[0]) and abs(image[i][j] - image[u][v]) <= threshold: continue
            else: 
                return False 
        return True

    def cell5Check(i, j):
        for (u,v) in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= u < len(image) and 0 <= v < len(image[0]) and abs(image[i][j] - image[u][v]) <= threshold: continue
            else: 
                return False 
        return True
    def cell6Check(i, j):
        for (u,v) in [(i-1, j), (i+1, j), (i, j-1)]:
            if 0 <= u < len(image) and 0 <= v < len(image[0]) and abs(image[i][j] - image[u][v]) <= threshold: continue
            else: 
                return False 
        return True
    def cell7Check(i, j):
        for (u,v) in [(i-1, j), (i, j+1)]:
            if 0 <= u < len(image) and 0 <= v < len(image[0]) and abs(image[i][j] - image[u][v]) <= threshold: continue
            else: 
                return False 
        return True
    def cell8Check(i, j):
        for (u,v) in [(i-1, j), (i, j-1), (i, j+1)]:
            if 0 <= u < len(image) and 0 <= v < len(image[0]) and abs(image[i][j] - image[u][v]) <= threshold: continue
            else: 
                return False 
        return True
    def cell9Check(i, j):
        for (u,v) in [(i-1, j), (i, j-1)]:
            if 0 <= u < len(image) and 0 <= v < len(image[0]) and abs(image[i][j] - image[u][v]) <= threshold: continue
            else: 
                return False 
        return True


    def checkRegion(i, j):
        indexChecks =  [ (i, j), (i, j+1), (i, j+2), 
                        (i+1, j), (i+1, j+1), (i+1, j+2), 
                        (i+2, j), (i+2, j+1), (i+2, j+2)]

        cellChecks= [cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9]

        for w in range(9):
            u, v = indexChecks[w]
            cellCheck = cellChecks[w]
            if (u,v) in cellCheck: continue
            else: 
                # print("failed at " + str(u) + " , " + str(v))
                return False
        return True
        

    def calcAvgIntensity(i, j):
        indexChecks =  [ (i, j), (i, j+1), (i, j+2), 
                        (i+1, j), (i+1, j+1), (i+1, j+2), 
                        (i+2, j), (i+2, j+1), (i+2, j+2)]
        res = 0
        for w in range(9):
            u, v = indexChecks[w]
            res += image[u][v]
        return res//9
            


    cell1 = set()
    cell2 = set()
    cell3 = set()
    cell4 = set()
    cell5 = set()
    cell6 = set()
    cell7 = set()
    cell8 = set()
    cell9 = set()

    for i in range(len(image)):
        for j in range(len(image[0])):
            if cell1Check(i,j): cell1.add((i,j))
            if cell2Check(i,j): cell2.add((i,j))
            if cell3Check(i,j): cell3.add((i,j))
            if cell4Check(i,j): cell4.add((i,j))
            if cell5Check(i,j): cell5.add((i,j))
            if cell6Check(i,j): cell6.add((i,j))
            if cell7Check(i,j): cell7.add((i,j))
            if cell8Check(i,j): cell8.add((i,j))
            if cell9Check(i,j): cell9.add((i,j))            
    

    regions = dict()
    for i in range(len(image)-2):
        for j in range(len(image[0])-2):
            # print(i, j)
            if checkRegion(i, j): 
                regionIntensity = calcAvgIntensity(i, j)
                regions[(i, j)] = regionIntensity
            

    res = [[0 for _ in range(len(image[0]))] for _ in range(len(image))]
    countRegions = [[0 for _ in range(len(image[0]))] for _ in range(len(image))]

    # for each region, calculate teh average intensity 

    for (i, j) in regions.keys():
        for u, v in [ (i, j), (i, j+1), (i, j+2), 
                        (i+1, j), (i+1, j+1), (i+1, j+2), 
                        (i+2, j), (i+2, j+1), (i+2, j+2)]:
            # print(i, j)
            res[u][v] += regions[(i,j)]
            countRegions[u][v] += 1

    for i in range(len(image)):
        for j in range(len(image[0])):

            if res[i][j] > 0: res[i][j] = res[i][j] // (countRegions[i][j])
            if res[i][j] == 0: res[i][j] = image[i][j]

    return res


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

# image = [[1,14,9,2],[10,16,13,8],[7,11,12,4]]
# threshold = 13


# image = [[5,6,7,10],[8,9,10,10],[11,12,13,10]]

# threshold = 3

print(resultGrid(image, threshold))