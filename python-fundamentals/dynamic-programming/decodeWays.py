# 1142; 1213 --> 31 min

# trick is to think about what are the valid inputs for letters and how to handle 0's 
# apply a memoization for faster results

def numDecodings(s):

    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code = {}
    for i, char in enumerate(alpha):
        code[str(i+1)] = char
    memo = {}

    def helper(s, memo):
        if s in memo: 
            return memo[s]
        else: 
            if not s: 
                res = 1
            elif s[0] == '0': 
                res = 0
            elif len(s) == 1: 
                res = 1 
            elif len(s) >= 2:
                if s[:2] not in code: 
                    res = helper(s[1:], memo)
                else: 
                    res = helper(s[1:], memo) + helper(s[2:], memo)
            memo[s] = res
            return res
    return helper(s, memo)


# a = "111111111111111111111111111111111111111111111"
# print(numDecodings(a))


# 111 -> helper(11) + helper (1)
#     --> helper(1)