# abcdefgh

# efgh/abcd
# gh/ef  // cd/ab
# gh/fe  // cd/ba

# // these must be adjacent

# abcde 
# bcde / a

# de / bc // a 
from functools import lru_cache

@lru_cache((None))
def isScramble(s1, s2):
    if sorted(s1) != sorted(s2):
        return False
    if len(s1) == len(s2) and len(s1) < 4:
        return True
    for i in range(1, len(s1)):
        if ((isScramble(s1[:i], s2[:i]) and isScramble(s1[i:], s2[i:])) or 
            (isScramble(s1[:-i], s2[:-i]) and isScramble(s1[-i:], s2[-i:]))):
            return True
    return False    



@lru_cache((None))
def isScramble(s1, s2):

    n, m = len(s1), len(s2)
    if sorted(s1) != sorted(s2):
        return False
    if n < 4 or s1 == s2:
        return True
    f = isScramble
    for i in range(1, n):
        if f(s1[:i], s2[:i]) and f(s1[i:], s2[i:]) or \
           f(s1[:i], s2[-i:]) and f(s1[i:], s2[:-i]):
            return True
    return False

s1 = 'great'
s2 = 'rgeat'


s1 = "abcde"
s2 = "caebd"

# s1 = "abcdefghijklmn"
# s2 = "efghijklmncadb"

print(isScramble(s1, s2))