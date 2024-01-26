from collections import Counter

def validTicTacToe(board):

    def winningCond(char, board):
        for row in board: 
            if row == char*3: return True
        for i in range(0, 3):
            if board[0][i] == char and board[0][i] == board[1][i] and board[1][i] == board[2][i]: return True
        if board[0][0] == char and board[0][0] == board[1][1] and board[1][1] == board[2][2]: return True
        if board[0][2] == char and board[0][2] == board[1][1] and board[1][1] == board[2][0]: return True
        return False


    if winningCond("X", board) and winningCond("O", board): return False
    counts = Counter()
    counts["X"] = 0
    counts["O"] = 0
    for row in board: 
        for c in row: 
            if c != " ": counts[c] += 1
    if winningCond("X", board) and counts["X"] == counts["O"]: return False
    if winningCond("O", board) and counts["X"] == counts["O"] + 1: return False
    if counts["X"] == counts["O"] or counts["X"] == counts["O"] + 1: return True
    return False