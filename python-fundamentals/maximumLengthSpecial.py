from collections import Counter, defaultdict

# this does things in O(n) Space, O(nlogn) Time for sorting and maintaining a ehap
# It's too spacey. So we reduce below to O(1) space

# def maximumLength(s):
#     def findSpecial(s):
#         res = Counter()
#         cur = []
#         for char in s: 
#             if not cur or cur[0] == char: 
#                 cur.append(char)
#             else: 
#                 res[("".join(cur))] += 1
#                 cur = [char]
#         res[("".join(cur))] += 1
#         return res

#     specials = findSpecial(s)

#     specialKeys = [x for x in specials.keys()]
#     specialKeys.sort(key = lambda x: -len(x))
#     counter = Counter()

#     for specialKey in specialKeys:
#         numSpecials = specials[specialKey] 
#         k = len(specialKey)
#         char = specialKey[0]
#         for x in range(k, 0, -1):
#             curSpecial = char*x
#             counter[curSpecial] += (k + 1 - x) * numSpecials

#     specialKeys = [x for x in counter.keys()]
#     specialKeys.sort(key = lambda x: -len(x))
#     # print(len(counter), len(specialKeys), len(s))
#     # print(specialKeys)
#     # print(counter)
#     for candidate in specialKeys: 
#         if counter[candidate] >= 3: 
#             return len(candidate)
#     return -1

from heapq import heappush, heappop
from math import inf 

def maximumLength(s):

    def cInsert(specialKey, counter):
        k = len(specialKey)
        oldChar = specialKey[0]
        heappush(counter[oldChar], k)
        while len(counter[oldChar]) > 3: heappop(counter[oldChar])
        
    counter, cur = defaultdict(list), []

    # identify specials and put the length of the special in the letter-heap
    for char in s: 
        if not cur or cur[0] == char: 
            cur.append(char)
        else: 
            specialKey = "".join(cur)
            cInsert(specialKey, counter)
            cur = [char]

    specialKey = "".join(cur)
    cInsert(specialKey, counter)

    res = -inf
    for x in counter: 
        z = counter[x]
        z.sort(key = lambda x: -x)        

        # is this really the smoothest way to identify top three items? 
        if len(z) == 3 and z[0] == z[1] == z[2]:
            res = max(z[0], res)
        elif len(z) > 1 and z[0] == z[1] +1:
            res = max(z[0]-1, res) 
        elif len(z) > 1 and z[0] == z[1] and z[0] -1 > 0:
            res = max(z[0]-1, res) 
        elif z[0] - 2 > 0: 
            res = max(z[0] - 2, res)

    if res == -inf: return -1
    return res


# s = "jicja"
# s = "aaaa"
# s = "abcaba"
# s = "abcdef"
s = "aabbccddaaabbbcccdddaaaaaaaaaaaabbbbbbbbbcccccdddd"
print(maximumLength(s))