# longest common subset practice

# Intuition: 
# Our DP array represents the longest common subset up to letter i (of word a)
# and letter j (of word b).

# For each i in word a, compare that letter to each jth letter in word b. 
# If they're equal, then the LCS is 1 + LCM(i-1, j-1). 
# (the prior letter in word a and b).

# O(mn) Time 
# O(mn) Space

def lcs(a, b):

    dp = [[0 for _ in range(len(b))] for _ in range(len(a))]

    maxLength = 0
    for i in range(len(a)):
        for j in range(len(b)):
            res = 0
            if a[i] == b[j]:
                if j == 0 or i == 0: res = 1
                else: res = 1 + dp[i-1][j-1]
            dp[i][j] = res
            maxLength = max(maxLength, res)
    print(dp)
    return maxLength

# can create a space optimized O(m) space since you only use current and previous rows of the 
# full 2d dp array. 


a = "abcdeabaeebbb"
b = "baceabcdeabccc"

print(lcs(a, b))