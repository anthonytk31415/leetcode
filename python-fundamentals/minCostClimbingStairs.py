# minCostClimbingStairs

def minCostClimbingStairs(cost):
    track = {}
    for i in range(len(cost)-1, -1, -1):
        if i + 1 >= len(cost) and i + 2 >= len(cost):
            x = 0
        elif i + 2 >= len(cost):
            x = min(track[i+1], 0)
        else: 
            x = min(track[i + 1], track[i + 2])
        track[i] = cost[i] + x
    return min(track[0], track[1])

# print(minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))


print(minCostClimbingStairs([10,15,20]))