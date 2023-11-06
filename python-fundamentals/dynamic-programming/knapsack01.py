# 0/1 knapsack

# given n items, choose the combination of the n items that yield the maximum profit 

# weights = array where weights[i] = weight of ith item
# profits = array where profits[i] = profit of ith item
# wt = total weight (i.e. capacity)
# n = # items

# Time: O(len(w) * n )
# Space: O(len(w) * n )



def knapsack(profits, weights, wt, n):
    profits = [0] + profits                                     # adjust profits, weights so they are 1-indexed
    weights = [0] + weights                                         
    knapsack = [[0 for _ in range(wt+1)] for _ in range(n+1)]   # instantiate with 0 in col and row 0; 
                                                                # row from 1-n, col from 1-w
    for i in range(n+1):                                        # each time you iterate a row, you check if you can do improve profits with a new weight
        for w in range(wt+1):                                   # so you consider max of last row at that weight capacity, or new weight + remainder
            if i == 0 or w == 0: 
                knapsack[i][w] = 0
            elif weights[i] <= w:                               # check if weights[i] a candidate to add into the knapsack
                knapsack[i][w] = max(knapsack[i-1][w], 
                                     knapsack[i-1][w-weights[i]] + profits[i])
            else: 
                knapsack[i][w] = knapsack[i-1][w]

    ## which objects to include: 
    include = [False]*(n+1)
    cur_profit = knapsack[n][w] 
    for i in range(n, 0, -1):
        if (cur_profit in knapsack[i] and                       # if that profit is in the current row but not in previous row,
            cur_profit not in knapsack[i-1]):                   # that profit was a result of including the weight_i
            include[i] = True
            cur_profit = cur_profit - profits[i]

    return knapsack[n][w], include



profits = [1,2,5,6]
weights = [2,3,4,5]
wt = 8
n = len(profits)
print(knapsack(profits, weights, wt, n))



## this version is you have unlmited weights you can put in
def knapsack(profit, weights, limit):
    dp = [[0]*(limit+1) for _ in range(len(weights)+1)]
    # print(dp)
    for i in range(1, len(dp)):
        for w in range(1, len(dp[0])):
            if w - weights[i-1] >= 0 : 
                dp[i][w] = max(dp[i-1][w], profit[i-1] + dp[i][w - weights[i-1]])
            else: 
                dp[i][w] = dp[i-1][w]

    print(dp)
    return dp[-1][-1]