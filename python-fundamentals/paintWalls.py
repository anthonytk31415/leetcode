# def paintWalls(cost, time): 

#     costToTime = []

#     for k in range(len(cost)):
#         costToTime.append((cost[k] / time[k], k))
    
#     costToTime.sort(key= lambda x: x[0])

#     print(costToTime)
#     curTime = 0
#     curScore = 0
#     i = 0
#     j = len(cost)-1
#     while i <= j: 
#         if curTime == 0: 
#             idx = costToTime[i][1]
#             curScore += cost[idx]
#             curTime += time[idx] 
#             i += 1
#         else: 
#             j -= 1
#             curTime -= 1
#     return curScore
from math import inf

# def paintWalls(cost, time):
#     n = len(cost)
#     dp = [0] + [inf] * n
#     for c, t in zip(cost, time):
#         for j in range(n, 0, -1):
#             dp[j] = min(dp[j], dp[max(j - t - 1, 0)] + c)
#         print(dp, c, t)
#     return dp[n]

def paintWalls(cost, time):
    n = len(cost)
    dp = [0] + [inf]* n

    for i in range(len(cost)):
        c = cost[i]
        t = time[i]
        for j in range(n, 0, -1):
            dp[j] = min( dp[j], dp[max(0, j - t -1)] + c)

    return dp[n]


# cost = [2,3,4,2]
# time = [1,1,1,1]

# cost = [1,2,3,2]
# time = [1,2,3,2]


# output: 77; exp: 63

cost = [42,8,28,35,21,13,21,35]
time = [2,1,1,1,2,1,1,2]
print(paintWalls(cost, time))