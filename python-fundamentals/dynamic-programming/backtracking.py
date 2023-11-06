# z = 'abc
# combination

## combinations via backtracking
def backtrack(str):
    res = []
    def helper(str, res, cur):
        if not str: 
            return 
        for i in range(len(str)): 
            res.append(cur + str[i])
            helper(str[i+1:], res, cur + str[i])
    helper(str, res, '')
    return res

print(backtrack('abc'))

# a different way to write this, but not as fundamental
def combination(arr):
    res = ['']
    for x in arr: 
        new_res = [y + x for y in res]
        res = res + new_res
    return res

print(combination('abc'))