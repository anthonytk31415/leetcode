# isValidSudoku

def isValidSudoku(board):
    rows = {}
    columns = {}
    central = {}
    for i in range(len(board)):
        rows[i] = set()
        columns[i] = set()
        central[i] = set()

    def build_central_assign():
        res = {}
        counter = 0
        defs = ((0,1,2), (3,4,5), (6,7,8))
        for i in defs:
            for j in defs:
                for a in i: 
                    for b in j: 
                        key = (a,b)
                        res[key] = counter
                counter += 1
        return res
    central_assign = build_central_assign()

    for i in range(len(board)):
        for j in range(len(board)):
            key = board[i][j]
            k = central_assign[(i,j)]
            if key =='.':
                continue
            if key in rows[i] or key in columns[j] or key in central[k]: 
                return False
            rows[i].add(key) 
            columns[j].add(key)
            central[k].add(key)
    return True



b1 = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]


# print(isValidSudoku(b1)) # true



b2 = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(b2)) #false

b3 = [
    [".",".",".",".","5",".",".","1","."],
    [".","4",".","3",".",".",".",".","."],
    [".",".",".",".",".","3",".",".","1"],
    ["8",".",".",".",".",".",".","2","."],
    [".",".","2",".","7",".",".",".","."],
    [".","1","5",".",".",".",".",".","."],
    [".",".",".",".",".","2",".",".","."],
    [".","2",".","9",".",".",".",".","."],
    [".",".","4",".",".",".",".",".","."]]


print(isValidSudoku(b3)) #false

## ibounds, jbounds 
# central = {
#     0: ((0,2),(0,2)),
#     1: ((0,2),(3,5)),
#     2: ((0,2),(6,9)),
#     3: ((3,5),(0,2)),
#     4: ((3,5),(3,5)),
#     5: ((3,5),(0,9)),
#     6: ((6,9),(0,2)),
#     7: ((6,9),(3,5)),
#     8: ((6,9),(0,9)),}  

# print(central)
# print(central[0][0])

# def central_assign(i,j):
#     central = {
#         0: ((0,2),(0,2)),
#         1: ((0,2),(3,5)),
#         2: ((0,2),(6,9)),
#         3: ((3,5),(0,2)),
#         4: ((3,5),(3,5)),
#         5: ((3,5),(0,9)),
#         6: ((6,9),(0,2)),
#         7: ((6,9),(3,5)),
#         8: ((6,9),(0,9)),}  

#     for key in central.keys():
#         print(key)
#         x = central[key][0]
#         y = central[key][1]
#         print(x, y)
#         if i >= x[0] and i <= x[1] and j >= y[0] and j <= y[1]:
#             return key
#     return False



def build_central_assign():
    res = {}
    counter = 0
    defs = ((0,1,2), (3,4,5), (6,7,8))
    for i in defs:
        for j in defs:
            for a in i: 
                for b in j: 
                    key = (a,b)
                    res[key] = counter
            counter += 1
    return res


central_assign = build_central_assign()

# print(mytable)

# print(mytable[(5,2)])