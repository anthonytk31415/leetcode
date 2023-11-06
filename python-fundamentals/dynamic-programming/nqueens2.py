# nqueens2


def isSafe(i,j,board):
    n = len(board)
# check vertical 
    for u in range(n):
        if i != u and board[u][j]=='Q':
            return False
# 4 conditions:
    # (1) traverse NW
    u, v = i-1, j-1
    while u >= 0 and v >= 0:
        if board[u][v] == 'Q':
            return False
        u -=1
        v -=1
    # (2) traverse SE
    u, v = i+1, j+1
    while u < n and v < n:
        if board[u][v] == 'Q':
            return False
        u +=1
        v +=1
    # (3) traverse SW
    u, v = i+1, j-1
    while u < n and v >=0:
        if board[u][v] == 'Q':
            return False
        u +=1
        v -=1    
    # (4) traverse NE
    u, v = i-1, j+1
    while u >=0 and v < n:
        if board[u][v] == 'Q':
            return False
        u -=1
        v +=1        
    return True





def solveNQueens(n): 
    res = []
    board = ['.'*n for x in range(n)]


    def dfs(board, i, res):
        if i == len(board):
            res.append(board)
            return 
        for j in range(len(board[0])):
            if isSafe(i,j,board):
                newBoard = [x for x in board]
                newBoard[i] = newBoard[i][:j] + 'Q' + newBoard[i][j+1:]       
                # print(f'board = {newBoard}, i={i}, j={j}')     
                dfs(newBoard, i+1, res)                

    dfs(board, 0, res)
    return res


print(solveNQueens(2))

# board = ['....', '....', '....', '....']


board1 = ['..Q.', 
          'Q...', 
          '...Q', 
          '....']

# print(isSafe(3,3, board1))

