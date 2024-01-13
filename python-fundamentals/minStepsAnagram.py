from collections import Counter

# traverse s and t to create a count of chars. then then for each char in t, if that char count is 
# different to the count is, it needs to be changed but only when count[t] > count[s] (to avoid double counting).abs

# Time: O(n) for traversing s, and t, and t again. 
# Space: O(n) for the length of s and t. 

def minSteps(s, t):
    sCounter, tCounter = Counter(s), Counter(t)
    res = 0
    for x in tCounter.keys(): 
        res += max(0, tCounter[x] - sCounter[x])
    return res

s = "leetcode"
t = "practice"
s = "anagram"
t = "mangaar"
    # return 
# a = Counter()
# a["b"] += 1



s = "aaacccddd"
t = "bbadddccc"

print(minSteps(s, t))

# b 2, 0 2
# a 1, 3 0
# c 0, 3 0
# d 3, 0 3
