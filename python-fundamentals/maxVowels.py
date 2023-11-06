
def isVowel(c):
    return (c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u')

def maxVowels(s, k):
    # first_word = str[:k]
    count_vowels = 0
    max_vowels = 0
    for c in s[:k]: 
        if isVowel(c):
            count_vowels +=1
    max_vowels = max(max_vowels, count_vowels)

    for i in range(k, len(s)):
        if isVowel(s[i - k]):
            count_vowels -=1
        if isVowel(s[i]):
            count_vowels +=1
        max_vowels = max(max_vowels, count_vowels)

    return max_vowels

s = "leetcode"
k = 3

print(maxVowels(s, k))