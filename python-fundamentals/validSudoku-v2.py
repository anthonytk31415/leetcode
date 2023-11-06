# 141
def isValidSudoku(board):

# for each iteration, create a dict and count occurances of non '.'; if any appear twice, --> False

    # for rows: 
    for i in range(len(board)):
        lookup = set()
        for j in range(len(board[0])):
            if board[i][j] not in lookup and board[i][j] != '.': 
                lookup.add(board[i][j])
            elif board[i][j] in lookup:

                return False

    # for columns: 
    for j in range(len(board[0])):
        lookup = set()
        for i in range(len(board)):
            if board[i][j] not in lookup and board[i][j] != '.': 
                lookup.add(board[i][j])
            elif board[i][j] in lookup:
                # print('(2)')
                return False


    bucket = [[0,1,2], [3,4,5], [6,7,8]]

    # for 3x3 cell: 
    for i in bucket: 
        for j in bucket:
            lookup = set() 
            for u in i: 
                for v in j: 
                    if board[u][v] not in lookup and board[u][v] != '.': 
                        lookup.add(board[u][v])
                    elif board[u][v] in lookup: 
                        # print('(3)')
                        return False
    return True

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))