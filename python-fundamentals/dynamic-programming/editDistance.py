# https://leetcode.com/problems/edit-distance/description/

# accommodate for 3 cases: 

# real tricky dp --> multiple scenarios to consider

# when letter1 != letter2, take min of botttom, + 1: 
# (1) dp[i][j-1] --> indicates i is taken care of, remove 1 letter from j
# (2) dp[i-1][j-1] --> indicates i-1 equal to j-1, add letter to make j-1 + {letter} equal to i
# (3) dp[i-1][j] --> indicates you have i-1 letters taken care of with j letters, so add one to take care of i letters


def minDistance(word1, word2):

    # dp represents min operations to make the word1 up to i equal to word2 up to j
    dp = [[0 for _ in range(len(word1) + 1)] for _ in range(len(word2) + 1)]

    dp[0] = [x for x in range(len(word1)+ 1)]

    for i in range(0, len(dp)):
        dp[i][0] = i

    # print(dp)
    for i in range(1, len(dp)): 
        letter2 = word2[i-1]
        for j in range(1, len(dp[0])):
            letter1 = word1[j-1]
            if letter1 == letter2: 
                dp[i][j] = dp[i-1][j-1]
            else: 
                dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
    # print(dp)
    return dp[-1][-1]


# word1 = "horse"
# word2 = "ros"
word1 = "intention"
word2 = "execution"
# word1 = "a"
# word2 = "ab"

print(minDistance(word1, word2))