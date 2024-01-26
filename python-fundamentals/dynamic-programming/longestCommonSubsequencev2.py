def longestCommonSubsequence(text1, text2):
    memo = {}

    def dfs(i, j):
        if (i,j) in memo: return memo[(i, j)]
        res = 0
        if i >= len(text1) or j >= len(text2): return res
        if text1[i] == text2[j]: res = 1 + dfs(i+1, j+1)
        else: 
            res = max(dfs(i, j+1), dfs(i+1, j))
        
        memo[(i,j)] = res
        return res

    return dfs(0,0)

text1 = "abcde"
text2 = "ace" 

text1 = "abc"
text2 = "def"

text1 = "supercalif"
text2 = "zzzzzzzsuperiiicalibbbb"

print(longestCommonSubsequence(text1, text2))