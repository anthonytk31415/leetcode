from collections import Counter

# this is currently O(n^2) Time but we could probably optimize it

def countPalindromicSubsequence(s):

    def countPalindromes(letter):
        left = 0
        right = len(s) - 1
        while True: 
            if s[left] != letter:
                left += 1
            else: 
                break
        while True: 
            if s[right] != letter:
                right -= 1
            else: 
                break
        countDistinctBetweenLetters = Counter(s[left + 1:right])
        return len(countDistinctBetweenLetters)


    countLetters = Counter(s)
    res = 0
    for letter in countLetters.keys():
        if countLetters[letter] > 1: 
            res += countPalindromes(letter)
    return res

s = "bbcbaba"
s = "adc"
s = "aabca"
print(countPalindromicSubsequence(s))