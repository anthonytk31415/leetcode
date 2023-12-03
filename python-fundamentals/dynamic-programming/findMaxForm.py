from collections import Counter

# Use 2-D DP Knapsack Technique. 
# Each str needs to iterate over possible m/n combinations. 
# You can save space by using two dp tables, a previous and a current, which is necessary for the problem.
# Time: O(m*n*len(strs)); Space: O(m*n)

def findMaxForm(strs, m, n):
    counts = {}
    strs = strs
    for char in set(strs):  
        counts[char] = Counter(char)

    dpPrev = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(len(strs)):
        cost_zero = counts[strs[i]].get("0", 0)
        cost_one = counts[strs[i]].get("1", 0)
        for zeroes in range(m + 1): 
            for ones in range(n + 1):
                z = 0
                if cost_zero <= zeroes and cost_one <= ones: 
                    z = 1 + dpPrev[zeroes - cost_zero][ones - cost_one]
                dp[zeroes][ones] = max(z, dpPrev[zeroes][ones])

        dpPrev, dp = dp, [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    return dpPrev[-1][-1]



# strs = ["10","0001","111001","1","0"]
# m = 5
# n = 3

# strs = ["10","0","1"]
# m = 1
# n = 1


strs = ["1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101"]

# # print(len(strs))
m = 100
n = 100
# 10000 * 526
print(findMaxForm(strs, m, n))





# this uses lenStr * m * n space. O(m*n) Time. TLE for probably cache reasons.
def findMaxForm1(strs, m, n):

    dp = {}
    counts = {}
    strs = [""] + strs
    for char in set(strs):  
        counts[char] = Counter(char)

    for i in range(len(strs)):
        cost_zero = counts[strs[i]].get("0", 0)
        cost_one = counts[strs[i]].get("1", 0)
        for zeroes in range(m + 1): 
            for ones in range(n + 1):
                idx = (zeroes, ones)
                if i == 0 or (zeroes == 0 and ones == 0): 
                    dp[(i, idx)] = 0
                else: 
                    x = dp.get((i, (zeroes - 1, ones)), 0)
                    y = dp.get((i, (zeroes, ones - 1)), 0)
                    z = 0
                    if cost_zero <= zeroes and cost_one <= ones: 
                        z = 1 + dp[(i-1 , (zeroes - cost_zero, ones - cost_one))]
                    dp[(i, idx)] = max(x, y, z, dp[(i-1 , idx)])

    return dp[(len(strs)-1, (m, n))]