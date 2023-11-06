# n queens 

# given n for an n x n board, : return all configurations where n queens can be placed without attacking each other

# basically try all 

def isSafe(board, i, j):
    # horizontal check 
    for v in range(len(board)):
        if j != v and board[i][v] == 1: 
            return False
    # vertical check 
    for u in range(len(board)):
        if i != u and board[u][j] == 1: 
            return False
    # for downslope diagonal going up: 
    u, v = i, j
    while True: 
        u -=1
        v -=1
        if u == -1 or v == -1: 
            break 
        if board[u][v] == 1:
            return False
    # for downslope diagonal going down: 
    u, v = i, j
    while True: 
        u +=1
        v +=1
        if u == len(board) or v == len(board): 
            break 
        if board[u][v] == 1:
            return False

    # for upward diagonal going down: 
    u, v = i, j
    while True: 
        u -=1
        v +=1
        if u == len(board) or v == len(board): 
            break 
        if board[u][v] == 1:
            return False
    # for upward diagonal going up
    u, v = i, j
    while True: 
        u +=1
        v -=1
        if u == len(board) or v == len(board): 
            break 
        if board[u][v] == 1:
            return False
    return True


def nQueens(n):
    board = [[0 for col in range(n)] for row in range(n)]
    res = []

    def helper(board, j, res):
        board = [x for x in board]
        if j == len(board[0]):
            res.append(board)
            # print(res)
            return 
        for z in range(len(board)):
            if isSafe(board, z,j):
                # print(f'position {z}, {j} is valid')
                board[z][j] = 1
                # print(board)
                helper([[y for y in x] for x in board], j+1, res)
                board[z][j] = 0
    helper(board, 0, res)
    if not res: 
        return False
    return res


# board = [[0 for _ in range(4)] for _ in range(4)]
# z = [[y for y in x] for x in board]
# z[1][2] = 1

# print(z)
# print(board)

print(nQueens(6))


# print(isSafe([[0,0,1],
#               [0,0,0],
#               [0,0,0]], 1,0)) # true
# print(isSafe([[0,0,1],
#               [0,0,0],
#               [0,0,0]], 2,0)) # false

# print(isSafe([[0,1,0,0],
#               [0,0,0,0],
#               [1,0,0,0],
#               [0,0,1,0]], 1,3)) # True