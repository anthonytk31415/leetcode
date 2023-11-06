# ex: 
# 3x2 --> 3x4
# 

from collections import defaultdict
def findDiagonalOrder(mat):
    diags = defaultdict(list)
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            diags[i + j + 1].append(mat[i][j])
    
    keys = list(diags.keys())
    keys.sort()
    res = []
    for x in keys:
        if x %2 == 1: 
            diags[x] = diags[x][::-1]
            res = res + diags[x]
        else: 
            res = res + diags[x]
    return res



def findDiagonalOrder3(mat):
    if len(mat[0]) == 1: 
        res = []
        for x in mat: 
            res = res + x
        return res

    if len(mat) == 1:
        return mat[0]


    rows = len(mat)        
    cols = len(mat[0])  + (rows - 1)
    diags = []
    
    for j in range(cols): 
        cur_diag = []
        i = 0 
        for _ in range(rows):
            print(i,j)
            if 0 <= i < len(mat) and 0 <= j < len(mat[0]): 
                cur_diag.append(mat[i][j])
            i +=1
            j -=1
        diags.append(cur_diag)
    for i in range(len(diags)):
        if i %2 == 0: 
            diags[i] = diags[i][::-1]
    res = []
    for x in diags: 
        res = res + x
    return res


mat = [[1,2,3],[4,5,6],[7,8,9]]
# mat = [[1,2],[3,4]]
print(findDiagonalOrder(mat))

def findDiagonalOrder2(mat):
    if len(mat) <= 1: 
        return mat[0]
    rowMax, colMax = len(mat)-1, len(mat[0]) - 1
    cur = [0,0]
    add_ind = 0     # 0: -1,+1; 1: +1,-1
    rd_ind = 0      # 0: right, 1 = down

    counter = 0
    maxcounter = len(mat)*len(mat[0])
    res = []
    add_dir = [[-1, 1], [1,-1]]
    rd_dir = [[0, 1], [1, 0]]
    

    while counter < maxcounter:
        print('counter = ', counter)
        print(cur, 'add_ind:', add_ind, 'rd_ind:', rd_ind)
        res.append(mat[cur[0]][cur[1]])
        i, j = cur

        if not (0 <= i + add_dir[add_ind][0] <= rowMax) or not (0 <= j + add_dir[add_ind][1] <= colMax):
            if tuple(cur) in set([(0,colMax), (rowMax, 0)]):
                rd_ind = 1 - rd_ind

            print('this', 'coords', i, j, rd_dir[rd_ind][0],rd_dir[rd_ind][1] )
            cur = [i + rd_dir[rd_ind][0], j + rd_dir[rd_ind][1]]
            # print(cur)
            rd_ind = 1 - rd_ind
            add_ind = 1 - add_ind   
        else: 
            print('else clause', 'coords', i,j)
            cur = [i + add_dir[add_ind][0], j + add_dir[add_ind][1]]
        counter +=1
    return res

# mat = [[1,2,3],[4,5,6],[7,8,9]]
# mat = [[1,2],[3,4]]
# mat = [[2,3]]
# mat = [[2,5],[8,4],[0,-1]]
# print(len(mat))
# print(findDiagonalOrder(mat))