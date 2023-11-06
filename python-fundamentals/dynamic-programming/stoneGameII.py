from functools import lru_cache
from math import inf 

def stoneGameII(piles):

    for i in range(1, len(piles)):
        piles[i] = piles[i] + piles[i-1]

    piles = tuple([0] + piles)
    # print('lenth of piles: ', len(piles))

    @lru_cache(None)   
    def helper(curPlayer, scoreA, scoreB, cur, m, piles):
        print(curPlayer, scoreA, scoreB, 'cur:', cur, 'm:', m)
        if cur >= len(piles)-1: 
            return (scoreA, scoreB)

        maxMove = []

        for i in range(1, 2*m + 1):
        
            if cur + i >= len(piles):
                break
            
            piles_taken = piles[i + cur] - piles[cur]
        
            if curPlayer == 'A':
                print('(1) triggered')
                cur_res = helper('B', scoreA + piles_taken, scoreB, i + cur, max(m, i), piles)
            else: 
                print('(2) triggered')
                cur_res = helper('A', scoreA, scoreB + piles_taken, i + cur, max(m, i), piles)
        
            print(cur_res)
            maxMove.append(cur_res)
        

        print('maxmove: ', maxMove)

        if curPlayer == 'A':
            idx = None
            maxA = -inf
            for i in range(len(maxMove)):
                if maxA < maxMove[i][0]:
                    maxA = maxMove[i][0]
                    idx = i
            maxB = maxMove[idx][1]

        if curPlayer == 'B':
            idx = None
            maxB = -inf
            for i in range(len(maxMove)):
                if maxB < maxMove[i][1]:
                    maxA = maxMove[i][1]
                    idx = i
            maxA = maxMove[idx][0]

        return (maxA, maxB)
         
    return helper('A', 0, 0, 0, 1, piles)

piles = [1,2,3]
print(stoneGameII(piles))