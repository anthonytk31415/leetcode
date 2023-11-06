# longestPalindrome


def longestPalindrome(s):
    odd = set([x for x in s])
    even = [ (x + x) for x in s if (x + x) in s]
    print(odd)
    print(even)



s1 = 'abba'
s2 = 'babad'

print(longestPalindrome(s1))
print(longestPalindrome(s2))