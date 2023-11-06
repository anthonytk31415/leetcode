# Time: O(n)
# Space: O(n) for the result; O(1) otherwise


##########################################
## Part 1
##########################################
def create_letter_grid(s):
    res = []
    s = s.split(' ')
    for word in s: 
        cur = []
        for char in word: 
            cur.append(char)
        res.append(cur)
    return res

s = "ABBA UBBU ALAN ALDA"
sq = create_letter_grid(s)
print(sq)

##########################################
## Part 2
##########################################

from collections import defaultdict
from itertools import combinations

def valid_squares(sq):
    memo = defaultdict(defaultdict)
    for i in range(len(sq)):
        for j in range(len(sq[0])): 
            char = sq[i][j]
            memo[char][i] = set()                   # a set is a hash set; think of it as a valueless hash table with just keys that checks for membership in constant time

    for i in range(len(sq)):
        for j in range(len(sq[0])): 
            char = sq[i][j]
            memo[char][i].add(j)

    res = []
    for char in memo: 
        for row in memo[char]:
            combos = combinations(memo[char][row], 2)
            for x in combos: 
                length = abs(x[1] - x[0])
                if (row + length) in memo[char] and x[1] in memo[char][row + length] and x[0] in memo[char][row + length]:
                    res.append([char, (row, x[0]), (row, x[1]), (row + length, x[0]), (row + length, x[1])])

    return res

print(valid_squares(sq))
####################################################################################
# code for combination; can do this on a set by definidng a = list(_the_set)
# for a 2-length 
####################################################################################
a = [1,2,3]
res1 = []
for i in range(len(a)):
    for j in range(i+1,len(a)):
        res1.append((a[i],a[j]))
print(res1)

# for a 3-length combination (for fun)
a = [1,2,3,4]
res2 = []
for i in range(len(a)):
    for j in range(i+1, len(a)):
        for k in range(j+1, len(a)):
            res2.append((a[i], a[j], a[k]))
print(res2)


##########################################
## Part 3 
##########################################