
# DP problem. The setup is quite tedious but the solution is super clean. 
# You must mark down the derivation and see that for each k, for each i, the dp[k][i] = sum of dp[k-1] all the way up to i-1 + dp[k][i-1]
# because of the sum, at the end of our dpCur loop, we recreate a prefix sum array to get cumulative sums in constant time. 

# Time: O(N*K)
# Space: O(N)

def numberOfSets(n, k):
    res = 0
    dpPrev = [x*(x+1)//2 for x in range(n)]
    prefix = [x for x in dpPrev]
    for i in range(1, len(prefix)):
        prefix[i]= prefix[i] + prefix[i-1]
    dpCur = [0]*(n)

    for k in range(2, k+1):
        for i in range(1, len(dpCur)):
            dpCur[i] = dpCur[i-1] + prefix[i-1]
            
        dpPrev, dpCur = dpCur, [0]*(n)
        prefix = [x for x in dpPrev]
        for i in range(1, len(prefix)):
            prefix[i]= prefix[i] + prefix[i-1]

    return dpPrev[-1] % (10**9 + 7)

n = 30
k = 7

print(numberOfSets(n, k))