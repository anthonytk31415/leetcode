def countBattleships1(board):
    visited = set()
    def dfs(i, j):
        visited.add((i, j))
        for u, v in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= u < len(board) and 0 <= v < len(board[0]) and (u,v) not in visited and board[u][v] == "X": 
                dfs(u, v)

    count = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if (i, j) not in visited and board[i][j] == "X": 
                count += 1
                dfs(i, j)
    return count 


def countBattleships(board):
    count = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "X" and (j-1 < 0 or board[i][j-1] == ".") and (i-1 < 0 or board[i-1][j] == "."): 
                count += 1
    return count 


board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]

print(countBattleships(board))