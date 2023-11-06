# solveSudoku

# Time: O(9^N)
# Space: uses array in place; O(N) for 

# n = digit
def isSafe(i,j,num, board):
    num = str(num)
    n = len(board)
    lookup = {}
    three_nums = [[0,1,2],[3,4,5],[6,7,8]]
    for x in three_nums:
        for y in x: 
            lookup[y] = x

    # check rows
    for u in range(n):
        if u != i and board[u][j] == num: 
            return False

    # check cols
    for v in range(n):
        if v != j and board[i][v] == num:
            return False

    # check 3x3
    u_range, v_range = lookup[i], lookup[j]
    for u in u_range:
        for v in v_range:
            if u != i and v != j and board[u][v] == num:
                return False
    return True

# returns false if it has any '.' else True
def filled(board):
    for x in board: 
        if '.' in x: 
            return False
    return True

def next_cell(i,j,n):
    if j < (n-1): 
        j +=1
    elif j == n-1: 
        j = 0
        i +=1 
    return i,j

def solveSudoku(board):
    n = len(board)
    status = {'sol_found': False, 'sol': None}

    def dfs(board, i,j,n, status):                                # each call of dfs assumes the board "is safe"
        if status['sol_found'] == True:
            return 
        if filled(board):
            status['sol_found'] = True
            status['sol'] = board
            return
        elif board[i][j] == '.':                                  # fill it in 1-9 recursively on '.' 
            for z in range(1,n+1):                                # iterate from 1-9, recursively
                if isSafe(i,j,z,board):                           # confirm the entry is safe
                    board[i][j]= str(z)                       # adjust this code so it actually works !!!
                    i_new,j_new = next_cell(i,j,n)
                    dfs(board, i_new,j_new,n, status)
                    if status['sol_found'] == False: 
                        board[i][j]= '.'
        else:                                                     # skip to the next cell
            i_new,j_new = next_cell(i,j,n)
            dfs(board, i_new,j_new,n, status)
    dfs(board, 0, 0, n, status)

    # print(status['sol'])
    # for i in range(n):
    #     for j in range(n):
    #         board[i][j] = status['sol'][i][j]

board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

# Solution?
# [['5', '3', '4', '6', '7', '8', '9', '1', '2'], 
#  ['6', '7', '2', '1', '9', '5', '3', '4', '8'], 
#  ['1', '9', '8', '3', '4', '2', '5', '6', '7'], 
#  ['8', '5', '9', '7', '6', '1', '4', '2', '3'], 
#  ['4', '2', '6', '8', '5', '3', '7', '9', '1'], 
#  ['7', '1', '3', '9', '2', '4', '8', '5', '6'], 
#  ['9', '6', '1', '5', '3', '7', '2', '8', '4'], 
#  ['2', '8', '7', '4', '1', '9', '6', '3', '5'], 
#  ['3', '4', '5', '2', '8', '6', '1', '7', '9']]

# new_board = [[y for y in x] for x in board]
# print(new_board)
# board2 = [[1,2,3,4,5,6,7,8,9],
#           [1,2,3,4,5,6,7,8,9],
#           [1,2,3,4,5,6,7,8,9]]

# print(isSafe(1,2,3, board))
# print(filled(board2))
solveSudoku(board)
# x = dfs(board, 0,0,9)
print(board)


# print(next_cell(8,2,9))