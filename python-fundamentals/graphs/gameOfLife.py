def gameOfLife(board):
    new_board = [[None for col in range(len(board[0]))] for row in range(len(board))]
    neighbor_coords = [(-1,-1), (-1,1), (1,-1), (1,1), (1,0), (-1,0), (0,-1), (0,1)]
    for i in range(len(board)):
        for j in range(len(board[0])):
            num_dead = 0
            num_alive = 0
            for pair in neighbor_coords:
                x,y = pair
                u, v = x+i, y+j
                if 0 <= u < len(board) and 0 <= v < len(board[0]):
                    if board[u][v]==0: 
                        num_dead +=1
                    else: 
                        num_alive +=1
            if board[i][j] ==1: 
                if num_alive < 2: 
                    new_board[i][j] = 0 
                elif 2 <= num_alive <= 3: 
                    new_board[i][j] = 1
                elif num_alive > 3: 
                    new_board[i][j] = 0 
            else: 
                if num_alive == 3: 
                    new_board[i][j] = 1
                else: 
                    new_board[i][j] = 0
    for i in range(len(board)):
        board[i] = new_board[i]
    return 
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]

print(gameOfLife(board))
print(board)