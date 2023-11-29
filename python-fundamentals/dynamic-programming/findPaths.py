# https://leetcode.com/problems/out-of-boundary-paths/

# Create a memo for the cell, number of moves, to return the # of ways out
# DFS each move and decrement the move at each step. 


def findPaths(m, n, maxMove, startRow, startColumn):    
    memo = {}       # (i, j, num Moves) -> num exits

    def dfs(i, j, numMoves):
        if (i, j, numMoves) in memo: 
            return memo[(i, j, numMoves)]
        res = 0
        if numMoves > 0: 
            for u, v in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= u < m and 0 <= v < n: 
                    res += dfs(u, v, numMoves - 1)
                else: 
                    res += 1

        memo[(i, j, numMoves)] = res
        return res
    
    return dfs(startRow, startColumn, maxMove) % (10**9 + 7)


# m = 2
# n = 2
# maxMove = 2
# startRow = 0
# startColumn = 0

m = 1
n = 3
maxMove = 3
startRow = 0
startColumn = 1

print(findPaths(m, n, maxMove, startRow, startColumn))