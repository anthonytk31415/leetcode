def longestCommonSubsequencePractice(word1, word2):

    dp  = [[0 for _ in range(len(word2))] for _ in range(len(word1))]

    for i in range(len(dp)):
        for j in range(len(dp[0])):
            res = 0
            if word1[i] == word2[j]:
                if i == 0 or j == 0: res = 1
                else: res = 1 + dp[i-1][j-1]
            elif not (i == 0 or j == 0): 
                res = max(dp[i-1][j], dp[i][j-1])
            dp[i][j] = res 

    return dp[-1][-1]

# Time: O(mn) for m = len(word1), n = len(word2)
# space O(n) optimized

def longestCommonSubsequencePractice1(word1, word2):
    prev, cur  = [0]* len(word2), [0]* len(word2)

    for i in range(len(word1)):
        for j in range(len(word2)):
            res = 0
            if word1[i] == word2[j]:
                if j == 0: res = 1
                else: res = 1 + prev[j-1]
            elif j > 0: 
                res = max(prev[j], cur[j-1])
            cur[j] = res 
        prev, cur = cur, [0] * len(word2)

    return prev[-1]



word1 = "xxabraxxxxxxxcadabra" 
word2 = "zabrazzzzzcadabrazzzzz"

print(longestCommonSubsequencePractice1(word1, word2))