def letterCasePermutation(s):
    res = []

    def helper(s, res, path):
        if not s: 
            res.append(path)
            return 
        elif s[0].isnumeric(): 
            helper(s[1:], res, path + s[0])
        else:
            helper(s[1:], res, path + s[0].lower())
            helper(s[1:], res, path + s[0].upper())
    
    helper(s, res, '')
    return res

s = "a1b2"
print(letterCasePermutation(s))