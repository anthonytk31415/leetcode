from functools import lru_cache

# dp; interesting fact: first person always wins!

def stoneGame(piles):

    @lru_cache(None)
    def doMove(i, j):
        if i == j: 
            return (piles[i], 0)
        res = []
        if i+1 < len(piles): res.append(doMove(i+1, j))
        if j-1 >= 0: res.append(doMove(i, j-1))
        return max(doMove(i+1, j), doMove(i, j-1), key = lambda x: x[0])

    score, oppScore = doMove(0, len(piles)-1)
    return score > oppScore

piles = [5,3,4,5]
piles = [3,7,2,3]
piles = [6,10,10,6]
print(stoneGame(piles))