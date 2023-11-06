# To create a palindrome, pairs of characters are required to increase
# Can add a singular non-paired char in the middle 
# So count the pairs and add one remainder 
#
# O(n) time, O(n) storage

def longestPalindrome(s):
    # count the chars
    charCount = {}
    for char in s:
        if char in charCount:
            charCount[char] +=1
        else: 
            charCount[char] = 1
    # sum the pairs and then any remainder
    runningSum = 0    
    for x in charCount:
        pairs = int(charCount[x]/2)
        runningSum = runningSum + pairs
    ## collect a singular remainder
    for x in charCount: 
        if charCount[x] % 2 == 1:
            return runningSum*2 + 1
    return runningSum*2



    # if you have a remainder, that can be the in the middle of 
    # the palindrome so create an indicator

# s = "abccccdd"
# print(longestPalindrome(s))

# s = ""
# print(longestPalindrome(s))


# s = "a"
# print(longestPalindrome(s))


# s = "aAbBanthony trankiem BBA"
# print(longestPalindrome(s))

s = 'deified'
print(longestPalindrome(s))
