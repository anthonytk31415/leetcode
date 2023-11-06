# longest common subsequence 
# 
# time: O(m*n)
# space: O(m*n)


def lcc(a, b): 
    memo = {}  ## (i,j) = answer
    
    def helper(a, b, memo, i, j):
        if (i,j) in memo: 
            return memo[(i,j)]
        else: 
            res = None
            if i >= len(a) or j >= len(b): 
                res = 0
            elif a[i] == b[j]:
                res = 1 + helper(a,b,memo, i+1, j+1)
            else: 
                res = max(helper(a,b,memo, i+1, j), helper(a,b,memo,i,j+1))
            memo[(i,j)] = res
            return memo[(i,j)]
    
    return helper(a,b,memo,0,0)


a = 'anthony'
b = 'hon'
print(lcc(a,b))