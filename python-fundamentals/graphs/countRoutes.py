# https://leetcode.com/problems/count-all-possible-routes/?envType=daily-question&envId=2023-11-13


# brute force it: 
# begin at start and then dfs until you get to finish 
# if at any point you dont have enough fuel, terminate 


# what if you had a hash table of start, finish, fuel, and how many ways. 
# then for a given amount of fuel

# here's the brute force problem
from collections import deque

# brute force; 
# could use a memoizatoin with fuel using a dfs?
def countRoutes1(locations, start, finish, fuel):
    
    queue = deque([(start, fuel, [start])])
    winningPaths = set([])
    while queue:
        u, fuel, path = queue.popleft()
        if u == finish and tuple(path) not in winningPaths:  
            winningPaths.add(tuple(path))
        for v, num in enumerate(locations): 
            if v != u: 
                fuelCost = abs(locations[u] - num)
                if fuelCost <= fuel: 
                    queue.append([v, fuel - fuelCost, path + [v]])
    return len(winningPaths)

# here's the DP version
# Time: O(fuel * m locations)
# Space: O(m*n)
def countRoutes(locations, start, finish, fuel):

    dp = [[0 for _ in range(len(locations))] for _ in range(0, fuel + 1)]
    dp[0][finish] = 1
    # print(dp)
    for f in range(1, fuel + 1):
        for i in range(len(locations)):
            numEntrants = 0
            for j in range(len(locations)):
                if i != j: 
                    fuelCost = abs(locations[i] - locations[j])
                    if f - fuelCost >= 0: 
                        numEntrants += dp[f-fuelCost][j]
                        # print(f, i, numEntrants, "adding")
            if i == finish: 
                numEntrants += 1
            dp[f][i] = numEntrants
            # print(f, i, numEntrants)
    # print(dp)
    return dp[fuel][start]



locations = [2,3,6,8,4]
start = 1
finish = 3
fuel = 5


# locations = [5,2,1]
# start = 0
# finish = 2
# fuel = 3

# locations = [4,3,1]
# start = 1
# finish = 0
# fuel = 6
# 5

print(countRoutes(locations, start, finish, fuel))