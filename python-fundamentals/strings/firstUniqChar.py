from collections import Counter, defaultdict
from math import inf
def firstUniqChar(s):
    letters = defaultdict(int)
    for char in s: 
        letters[char] +=1


    for i in range(len(s)): 
        if letters[s[i]] == 1: 
            return i
    return -1

s = "anthony"

print(firstUniqChar(s))