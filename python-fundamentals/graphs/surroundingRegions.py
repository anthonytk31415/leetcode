# O(n) time - traverse all nodes
# O(n) space to keep track of visited nodes

# dfs approach for each connected component

def solve(board):
    visited = set()

    # visits all connecting 'O' cells and returns a "path" of all traversed nodes 
    # 
    def dfs(row, col, board, border, path, visited):
        visited.add((row, col))
        path.add((row, col))
        ## mark if current cell touches a border
        for (u,v) in [(row-1, col),(row+1, col),(row, col-1),(row, col+1)]:
            if not border[0] and (u < 0 or u >= len(board) or v < 0 or v >= len(board[0])):
                border[0] = True
        ## traverse 
        for (u,v) in [(row-1, col),(row+1, col),(row, col-1),(row, col+1)]:
            if (u,v) not in visited and u >= 0 and u < len(board) and v >= 0 and v < len(board[0]) and board[u][v] == 'O':                
                dfs(u, v, board, border, path, visited)

    for row in range(len(board)):
        for col in range(len(board[0])):
            
            if (row, col) not in visited: 
                if board[row][col] == 'O':
                    path = set()
                    border = [False]
                    dfs(row, col, board, border, path, visited)
                    if not border[0]: 
                        for (u,v) in path: 
                            board[u][v] = 'X'
                else: 
                    visited.add((row, col))
    return board

board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

print(solve(board))