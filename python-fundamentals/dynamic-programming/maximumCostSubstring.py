# kadane's max sum subarray

def maximumCostSubstring(s, chars, vals):
    charVals = {}
    i = 1
    for x in "abcdefghijklmnopqrstuvwxyz": 
        charVals[x] = i
        i += 1
    for i, x in enumerate(chars):
        charVals[x] = vals[i]

    dp = [0]*len(s)
    dp[0] = max(0, charVals[s[0]])
    overallMax = max(0, dp[0])
    for i in range(1, len(s)): 
        x = s[i]
        dp[i] = max(dp[i-1] + charVals[x], 0, charVals[x])
        overallMax = max(dp[i], overallMax)
    return overallMax

s = "adaa"
chars = "d"
vals = [-1000]

s = "abc"
chars = "abc"
vals = [-1,-1,-1]

print(maximumCostSubstring(s, chars, vals))