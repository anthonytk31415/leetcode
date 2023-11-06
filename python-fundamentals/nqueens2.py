

def intersect(board, row, col, n):
    ## check row
    for j in range(n):
        if j != col and board[row][j] == 'Q': 
            return True

    ## check col
    for i in range(n):
        if i != row and board[i][col] == 'Q':
            return True

    ## check downslope diagonal 
    for d in range(-n+1, n):
        if d != 0 and 0 <= (row + d) < n and 0 <= (col + d) < n and board[row+d][col+d] == 'Q':
            return True 
    
    ## check upslope diagonal
    for d in range(-n+1, n):
        if d != 0 and 0 <= (row - d) < n and 0 <= (col + d) < n and board[row-d][col+d] == 'Q':
            return True 
    return False

board = [[None, None, None], ['Q', None, None], [None, 'Q', None]]

print(intersect(board, 2,1,3))


## checks if the board is valid i.e. no intersecting queens 
def valid_board(board,n):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 'Q' and intersect(board, row, col,n):
                return False
    return True 

from collections import defaultdict

def totalNQueens(n):
    res = []
    board = [[None]*n for _ in range(n)]

    # are there any queens in the (row, col) path?

    def helper(n, row, col, board, res):
        board[row][col] = 'Q'
        if valid_board(board,n):
            if row == n-1:                                      # board is completed
                completed_board = tuple([tuple(x) for x in board])
                res.append(completed_board)
            else: 
                for c in range(len(board[0])):
                    helper(n, row+1, c, board, res)            
        board[row][col] = None

    for c in range(len(board[0])):
        helper(n, 0, c, board, res)

    return len(res)

print(totalNQueens(8))
