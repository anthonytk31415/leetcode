from functools import lru_cache, reduce
from math import inf

# this is a bit weird DP problem, wtih heavy geometry. 

def minScoreTriangulation(values):

    @lru_cache(None)
    def dfs(i, j):
        if j - i <= 1: return 0
        res = inf
        for k in range(i +1, j):
            res = min(res, dfs(i, k) + dfs(k, j) + values[i]*values[j]*values[k])
        return res
    return dfs(0, len(values)-1)

values =(1,2,3)
# values = [3,7,4,5]
# values = [1,3,1,4,1,5]
# values = [2,2,2,2,1]
values = [17,97,74,55,68,64,46,48,9,2,70,39,52,31,86,2,31,8,28,78]
print(minScoreTriangulation(values))    