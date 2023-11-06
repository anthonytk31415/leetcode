def isInterleave(s1, s2, s3):
    memo = {}

    def helper(s1, s2, s3, memo):
        if not s1 and not s2 and not s3:
            return True
        if (s1, s2, s3) in memo: 
            return memo[(s1, s2, s3)]
        else: 
            res = []
            if s1 and s3 and s1[0] == s3[0]:
                res.append(helper(s1[1:], s2, s3[1:], memo))
            if s2 and s3 and s2[0] == s3[0]:
                res.append(helper(s1, s2[1:], s3[1:], memo))
            res = any(res)
            memo[(s1, s2, s3)] = res
            return res
    
    return helper(s1, s2, s3, memo)

# s1 = "aabcc"
# s2 = "dbbca"
# s3 = "aadbbcbcac"

s1 = "aabcc" 
s2 = "dbbca"
s3 = "aadbbbaccc"

print(isInterleave(s1, s2, s3))