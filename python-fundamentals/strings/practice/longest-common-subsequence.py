# lcs

# Trick: 
# - keep a pointer for i, j for for text1, text2, respectively
# - keep a memo 
# - if text1[i] and text2[j] are equal, then add 1 and look at i+1, j+1
# - if not, then your lcs is the max of recursive i, j+1 or j, i+1
# - if your i/j are out of bounds, return 0


# Time: O(m*n) - each length in m is checked with each length in n
# Space: O(m*n) - we're storing the pairs in the memo for faster processing time
def longestCommonSubsequence(text1, text2):
    memo = {}

    def helper(text1, text2, i, j, memo):
        if (text1, text2, i, j) in memo:
            return memo[(text1, text2, i, j)]

        if i >= len(text1) or j >= len(text2): 
            res = 0

        elif text1[i] == text2[j]: 
            res =  1 + helper(text1, text2, i+1, j+1, memo)

        elif text1[i] != text2[j]:
            res = max(helper(text1, text2, i, j+1, memo), helper(text1, text2, i+1, j, memo))

        memo[text1, text2, i, j] = res
        return res


    return helper(text1, text2, 0, 0, memo)

print(longestCommonSubsequence('anthony', 'hony'))