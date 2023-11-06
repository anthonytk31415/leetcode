#1050


# m x n board

# find all starting points: where word[0] == board[i][j]
# for each starting point, do dfs where cancidates 
# if you get to the end, return True

# Time: O(m*n*3^l) for m*n board and l = length of word and 3^l for each mxn position, you have 3 possible candidates (can't go back)
# Space: O(n) for each n candidate, n <= mxn but can be reduced to O(1); its for the queue

# trick: use the '#' on the board to prevent revisits

def exist(board, word):
    from collections import Counter

    ## check if the board contains enough chars for the word itself
    board_array = []
    for y in board: 
        board_array = board_array + y
    board_counter = Counter(board_array)
    word_counter = Counter(word)
    for c in word_counter: 
        if c not in board_counter or board_counter[c] < word_counter[c]: 
            return False

    def dfs(board, word, w):
        if not word:  
            return True
        (i,j) = w
        if i < 0 or i > len(board) - 1 or j < 0 or j > len(board[0])-1 or board[i][j] != word[0]:
            return False
        temp = board[i][j]
        board[i][j] = '#'           # temporarily change the entry to '#' to prevent revisit
        res = (dfs(board, word[1:], (i-1, j)) or dfs(board, word[1:], (i+1, j)) or
                dfs(board, word[1:], (i, j-1)) or dfs(board, word[1:], (i, j+1)))
        board[i][j] = temp          # reset to un-'#' for next iterations
        return res

    #iterate over the queue
    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(board, word, (i,j)): 
                return True
    return False
        

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"


# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "SEE"

# board = [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]]
# word = "AAAAAAAAAAAAAAa"
# print(board[0])
print(exist(board, word))