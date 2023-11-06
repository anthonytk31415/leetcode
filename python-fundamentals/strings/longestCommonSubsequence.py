def lcm(a, b):
    res = set()

    def helper(i, j, res, a, b, path):
        if i >= len(a) or j >= len(b):
            if path and path not in res:
                res.add(path)
            return 
        # only move foward in i and j if there's an equal char
        if a[i] == b[j]:
            helper(i+1, j+1, res, a, b, path + a[i])
        else:
            helper(i, j+1, res, a, b, path)

    # iterate over all chars in a; 
    for i in range(len(a)):
        helper(i, 0, res, a, b, '')

    return res

# print(lcm('aabacdddd', 'zzayybycya'))
X = "AGGTAB"
Y = "GXTXAYB"
# 4: GTAB
print(lcm(X, Y))

## run through each letter of x 
