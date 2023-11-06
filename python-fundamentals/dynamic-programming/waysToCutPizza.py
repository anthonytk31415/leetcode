# https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/


# Time: Time O(r*c*k*(r+c))
# Space(r*c*r*c)

from functools import lru_cache
from collections import Counter

## apply cut, and also find aples removed
def applyCut(curCut, pizza):
    dir, idx = curCut
    newPizza = [[col for col in row] for row in pizza]
    countApplesRemoved = 0

    if dir == 'row':
        for i in range(idx):
            for j in range(len(pizza[0])):
                if newPizza[i][j] == 'A': countApplesRemoved +=1
                newPizza[i][j] = '.' 

    elif dir == 'col':
        for i in range(len(pizza)):
            for j in range(idx):
                if newPizza[i][j] == 'A': countApplesRemoved +=1
                newPizza[i][j] = '.' 

    if countApplesRemoved == 0:
        return False
    return newPizza, countApplesRemoved

def ways(pizza, k):
    
    pizza = [[x for x in row] for row in pizza]     # convert array of strings --> array of arrays

    # cutWays = possible cuts currently; start with all cuts
    
    cutWays = set()
    for row in range(1, len(pizza)):
        cutWays.add(('row', row))
    for col in range(1, len(pizza[0])):
        cutWays.add(('col', col))
    allCuts = set([x for x in cutWays])
    # count apples
    countApples = 0
    for i in range(len(pizza)):
        curCount = Counter(pizza[i])
        countApples += curCount['A']

    # every time pizza is fed, it is a valid pizza i.e. it contains at least 1 apple
    # cutsLeft initialize with k - 1
    # 
    # print(cutWays)
    def dfs(pizza, cutsLeft, cutWays, countApples):
        # print('initial state: ', pizza, 'cuts left', cutsLeft)
        # mark terminal states
        if cutsLeft == 0 and countApples > 0:
            # print('winning combo', pizza, allCuts.difference(cutWays))
            return 1

        # you have too many cuts and not enough apples
        # if cutsLeft > countApples - 1:  
        #     return 0

        res = 0
        for curCut in cutWays:
            dir, idx = curCut
            # sliceToGive returns False if the slice to give does not have apples, if true, returns how many apples to remove
            pizzaCheck = applyCut(curCut, pizza)
            if pizzaCheck: 
                newPizza, countApplesRemoved = pizzaCheck   # returns the new pizza with x's at the cuts
            # print('exploring possibilities', pizzaCheck, curCut)
            if pizzaCheck != False and cutsLeft - 1 < countApples - countApplesRemoved:
                # print('dfs happens')
                newCutWays = set([x for x in cutWays])
                newCutWays.remove((dir, idx))                  # you're doing the cut so remove the 
                res += dfs(newPizza, cutsLeft - 1, newCutWays, countApples - countApplesRemoved)
        return res

    return dfs(pizza, k-1, cutWays, countApples) % (10**9 + 7)



# build a function that checks from x1 to x2, from y1 to y2 if it contains an apple. Cache it.
# then you'll dfs across 0 to len(pizza) and from 0 to len(pizza[0]). if the 
#
# terminal: if k == 1 (no more cuts) and you currently have an apple: return 1
# 



from functools import cache



def ways(pizza, k):
    m = len(pizza)
    n = len(pizza[0])

    @lru_cache(None)
    def check(x1, x2, y1, y2):
        for i in range(x1, x2):
            for j in range(y1, y2):
                if pizza[i][j] == 'A': return True
        return False

    @lru_cache(None)
    def dfs(x1, x2, y1, y2, k):
        if k == 1 and check(x1, x2, y1, y2):
            return 1

        res = 0
        for i in range(x1 + 1, x2):
            if check(x1, i, y1, y2) and check(i, x2, y1, y2):
                res += dfs(i, x2, y1, y2, k-1)
        for j in range(y1 + 1, y2):
            if check(x1, x2, y1, j) and check(x1, x2, j, y2):
                res += dfs(x1, x2, j, y2, k-1)

        return res


    return dfs(0,m, 0, n, k) % (10**9 + 7)







# class Solution:
#     def ways(self, pizza: List[str], k: int) -> int:

#         # From (x1, y1) To (x2, y2)
#         @cache
#         def check (x1,y1,x2,y2):
#             for r in range(x1, x2+1):
#                 for c in range(y1, y2+1):
#                     if pizza[r][c] == 'A':
#                         return True 
#             return False 
        
#         @cache
#         def dp (r, c, k):

#             if k == 1 :
#                 if check (r, c, len(pizza)-1, len(pizza[0])-1):
#                     return 1
            
#             cnt = 0 
#             for i in range(c+1, len(pizza[0])):
#                 if check (r, c, len(pizza)-1, i-1):
#                     cnt += dp (r, i, k-1)
#             for j in range(r+1, len(pizza)):
#                 if check (r, c, j-1, len(pizza[0])-1):
#                     cnt += dp (j, c, k-1)
#             return cnt 

#         return dp(0,0,k) % (10 ** 9 + 7)





# pizza = ["A..","AAA","..."] 
# k = 3
# pizza = ["A..","AA.","..."]
# k = 3


pizza = ["AAAA......A.AA.","AAAA.A.AAA..AA.","..AA.A.A.A.A...","A.AAAA.......A.","A.AA..A...AA...","A..A.AA.AA.A...",".A.A....AA.AAA.","AAAAAAA........","AAA.....AAA..AA","A.A.A.A...A..A.",".A.A.A.A.A..AA.","AAAA...A..A....",".A..AA.AAA..AAA",".AAAA.A.AAA.AAA","AA.A...A.AAAA..",".A.AAAA...A.AA.","A.A..AA.AA.....","..A......AAA.A.",".A..AAAAA....AA"]
k = 5
print(ways(pizza, k))


