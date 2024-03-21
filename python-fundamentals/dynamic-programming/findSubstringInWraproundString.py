# i solved this using sliding windows ; O(n) time, O(26) space

# how to do this in DP?

def findSubstringInWraproundString(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphaNext = {}
    alphaCount = {}
    for i, char in enumerate(alphabet):
        alphaCount[char] = 0
        if char == "z": alphaNext[char] = "a"            
        else: alphaNext[char] = alphabet[i+1] 

    left = 0
    right = 0    
    while left < len(s):
        while right + 1 < len(s) and alphaNext[s[right]] == s[right + 1]:
            right += 1
        
        # these are all valids 
        for i in range(left, right + 1):
            curChar = s[i]
            length = right - i + 1            
            alphaCount[curChar] = max(length, alphaCount[curChar])
        
        right += 1
        left = right

    res = sum([alphaCount[x] for x in alphaCount])
    return res

# s = "cac"
# s = "zaba"
s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyza"
print(findSubstringInWraproundString(s))


