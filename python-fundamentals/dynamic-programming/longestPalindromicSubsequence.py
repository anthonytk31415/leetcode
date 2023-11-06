# zyszzab

from functools import lru_cache
# if length == 0: return 0
# if length == 1: return 1
# if first and last are equal --> 2 + fn([a1:-1])

# return max(1:), max(:-1)

# time: o(n^2 )
# space: o(n)
def longestPalindromeSubseq(s):
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

# s = "bbbab"
# s = "cbbd"
s = 'supercalifragilisticexpealidocious'
print(longestPalindromeSubseq(s))


