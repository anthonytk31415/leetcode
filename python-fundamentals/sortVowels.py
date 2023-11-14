arr = ['E','e','O','e']
arr.sort()

print(arr)
from collections import deque

def sortVowels(s):
    word = list(s)
    vowels = set(['a','e','i','o','u','A','E','I','O','U'])
    strVowels = []
    for i, letter in enumerate(s):
        if letter in vowels: 
            strVowels.append(letter)
    strVowels.sort()
    strVowels = deque(strVowels)
    for i, letter in enumerate(word):
        if letter in vowels: 
            word[i] = strVowels.popleft()
    
    return ''.join(word)



s = "lEetcOde"
print(sortVowels(s))