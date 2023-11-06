from math import inf

# Time: O(3*max(days)*3)
# Space: O(3*max(days))

def minCostTickets(days, costs):
    costs = [0] + costs
    days_set = set(days)
    dp = [[inf]*(max(days)+1) for c in range(len(costs))]
    for c in range(len(costs)):
        dp[c][0] = 0
    day_diff = [0, 1, 7, 30]
    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if j in days_set: 
                min_considerations = []
                for ticket in range(1, i+1):
                    diff = 0
                    if j - day_diff[ticket] >= 0: 
                        diff = dp[i][j - day_diff[ticket]]
                    min_considerations.append(diff + costs[ticket])
                min_considerations.append(dp[i-1][j])
                dp[i][j] = min(min_considerations)
            else: 
                dp[i][j] = min(dp[i][j-1], dp[i-1][j])
    return dp[-1][-1]

# days = [1,4,6,7,8,20]
# costs = [2,7,15]

days = [1,2,3,4,5,6,7,8,9,10,30,31]
costs = [2,7,15]

print(minCostTickets(days, costs))