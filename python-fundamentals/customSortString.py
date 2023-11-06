# Time: O(n)
# Space: O(n)

from collections import Counter

def customSortString(order, s):
    count_s = Counter(s)
    res = ''
    for i in range(len(order)):
        if order[i] in count_s: 
            res = res + order[i] * count_s[order[i]]
            del(count_s[order[i]])
    for x in count_s: 
        res = res + x * count_s[x]
    return res

order = "cba"
s = "abcd"

print(customSortString(order, s))
