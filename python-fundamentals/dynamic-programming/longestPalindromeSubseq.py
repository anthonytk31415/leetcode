# DP using Longest Common Subsequence with a twist: for word2, use s[::-1]
# Otherwise, same logic: dp[i][j] = 1 + dp[i-1][j-1] if s[i] == s_reverse[j]
# not equal: take max of top and left

# Time: O(n^2)
# Spaec: O(n^2); can be optimized to O(n) --> see below

def longestPalindromeSubseq1(s):
    dp = [[0 for _ in range(len(s) + 1)] for _ in range(len(s) + 1)]
    sR = s[::-1]
    for i in range(1, len(s)+1):
        for j in range(1, len(s)+1):
            if s[i-1] == sR[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else: 
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]

# rewrite using O(n) space
def longestPalindromeSubseq(s):
    prev = [0 for _ in range(len(s) + 1)]
    cur = [0 for _ in range(len(s) + 1)]
    sR = s[::-1]
    for i in range(1, len(s)+1):
        for j in range(1, len(s)+1):
            if s[i-1] == sR[j-1]:
                cur[j] = 1 + prev[j-1]
            else: 
                cur[j] = max(prev[j], cur[j-1])
        prev, cur = cur, [0 for _ in range(len(s) + 1)]
    return prev[-1]

# another cute solution
def longestPalindromeSubseq2(self, s: str) -> int:
    @lru_cache(None)
    def helper(s):
        if len(s) == 0: 
            return 0
        elif len(s) == 1:
            return 1
        if s[0] == s[-1]:
            return 2 + helper(s[1:-1])
        else: 
            return max(helper(s[1:]), helper(s[:-1]))
    return helper(s)


s = "xxabzibai"

print(longestPalindromeSubseq(s))