# longestPalindrome

def longestPalindrome(s):
    hash = {}
    if len(s) == 1:
        return s[0]
    if len(s) > 1: 
        hash[1] = set([x for x in s])
    if len(s) >= 2: 
        hash[2] = set([ (x + x) for x in s if (x + x) in s])
    if len(s) == 2:
        if len(hash[2]) == 0:
            return s[0]
        else: 
            return next(iter(hash[2]))
    for i in range(3, len(s)+1, 1):
        # print(i, i+1)
        hash[i] = set([y + x + y for x in hash[i-2] for y in hash[1] if (y+x+y) in s]) #odd
        print(hash)
    for j in range(len(s), 0, -1):
        print(i, j)
        if j in hash and len(hash[j]) >0:
            return next(iter(hash[j]))
        print(hash)


# s0 = 'ab'
# s0 = 'aab'
# s0 = 'aba'
s0 = 'aa'
s1 = 'abba'
s2 = 'babad'
s3 =  'a'
s4 = 'asdoiuabababawerqewq'
s5 = 'aaaa'
# print(longestPalindrome(s0))
# print(longestPalindrome(s1))
# print(longestPalindrome(s2))
# print(longestPalindrome(s3))
# print(longestPalindrome(s4))
print(longestPalindrome(s5))