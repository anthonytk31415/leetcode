from math import inf

# Key Features: 
# - use memoization in i and m; note that we don't care about where you are currently with player points. to make the memoization efficient
# - at each step, the player will want to find the max outcome of each move of choosing j from 1 to 2m; so we call the funcion recursively
#   for each j decision, noting that the opponent will now make the optimal outcome (i.. we swich the points in the recursive call)
# - if your piles is less than 2*m, then take all of them



def stoneGameII(piles):
    # turn = 0 --> alice; turn = 1 --> bob
    memo = {}       ## store [playerPts, opponentPts]

    def takeTurn(i, m, playerPts, oppPoints):
        if (i, m) in memo: 
            res = memo[(i, m)]

        elif len(piles[i:]) <= 2*m: 
            res = [sum(piles[i:]), 0]
        else: 
            allMoves = []
            # print("i:", i, "m:", m)
            for j in range(1, 2*m + 1):
                newPts = sum(piles[i:i+j])
                allMoves.append(takeTurn(i + j , max(j, m), 0, 0 + newPts))     ## each allMove will return [playerPts, oppPots] from the opponents perspective

            maxIdx, maxPlayerMove = None, -inf
            for x, move in enumerate(allMoves): 
                if move[1] > maxPlayerMove: 
                    maxPlayerMove = move[1]
                    maxIdx = x
            oppMove = allMoves[maxIdx][0]
            res = [maxPlayerMove, oppMove]
            
            memo[(i, m)] = res
        
        a, b = res
        return [a + playerPts, b + oppPoints]

    return takeTurn(0, 1, 0, 0)[0]

# print(a + b)
# i = 2
# piles = [2,7,1]
# piles = [2,7,9,4,4]
# piles = [4,4,9,7,2]
# print(piles[:i+1])
piles = [1,2,3,4,5,100] ## 104
# piles = [7,5,9,9,9,9,5,1,8,6] ## 39
print(stoneGameII(piles))

# print(piles[0:1])