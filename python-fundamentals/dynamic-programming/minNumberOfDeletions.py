
# Time O(mn)
#O(mn) Space

# This is a variation of the Longest common subseqeunce problem. 

def minDistance1(word1, word2):

    dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]

    dp[0] = [x for x in range(0, len(word2) + 1)]
    for i in range(len(word1)+1):
        dp[i][0] = i

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if word1[i-1] != word2[j-1]:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
            else:
                dp[i][j] = dp[i-1][j-1]
    # print(dp)
    return dp[-1][-1]

# O(n) * 2 space optimization since we only use current and previous i's 


def minDistance(word1, word2):
    prev = [i for i in range(len(word2) + 1)]
    cur = [0 for _ in range(len(word2) + 1)]

    for i in range(1, len(word1) + 1):
        cur[0] = i
        for j in range(1, len(cur)):
            if word1[i-1] != word2[j-1]:
                cur[j] = 1 + min(prev[j], cur[j-1])
            else:
                cur[j] = prev[j-1]
        prev, cur = cur, [0 for _ in range(len(word2) + 1)]

    return prev[-1]

word1 = "abracadabra"
word2 = "abraabra"

print(minDistance(word1, word2))