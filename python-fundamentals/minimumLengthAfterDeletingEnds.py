from collections import deque

# this is a two pointers problem; but currently I build a deque to make it conveniently coded. I just count the characters into a deque. 
# and Pop left and right when they're equal. O(n) Time and Space. 

# there's an optimized version below using two pointers: O(n) Time, O(1) space. 

def minimumLength1(s):
    chars = []
    curChar = s[0]
    charCount = 1
    i = 1
    while i < len(s):
        if s[i] == curChar: 
            charCount += 1
        else: 
            chars.append((curChar, charCount))
            curChar = s[i]
            charCount = 1
        i += 1
    chars.append((curChar, charCount))

    chars = deque(chars)

    while len(chars) >1 and chars[0][0] == chars[-1][0]: 
        chars.popleft()
        chars.pop()
    
    if len(chars) == 1 and chars[0][1] > 1: 
        chars.pop()
    
    res = 0
    for x in chars: 
        res += x[1]
    return res



def minimumLength(s):
    i, j = 0, len(s) - 1
    while i < j:         
        if s[i] == s[j]:
            i += 1
            j -= 1

        elif s[i] != s[j]: 
            if i > 0 and s[i] == s[i-1]: i += 1
            elif j < len(s) - 1 and s[j] == s[j+1]: j -= 1
            else: break 

    if (i > j) or (i == j and len(s) > 2 and s[i] == s[i-1] == s[i+1]): return 0

    return j - i + 1




s = "cabaabac"
s = "aabccabba"
s = "ca"
s = "aabbccccaaaaabaaaccccbbbbba"
# s = 'a'
print(minimumLength(s))