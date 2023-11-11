# 2 pointers with memoization and dp/recursion 

# count the current length of consecutives
# then keep a running total of count homo's 
# count homo's is a recursive function: countHomo(n) = countHomo(n-1) + n; let's keep a memo of it

# Time: O(n)
# Space: O(n) for n max length of a homogonous unit 

def countHomogenous1(s):
    i = 0
    j = 0
    curLength = 0
    totalHomos = 0
    countHomoTracker = {1:1}

    def countHomo(k):
        if k in countHomoTracker: return countHomoTracker[k]
        res = countHomo(k-1) + k
        countHomoTracker[k] = res
        return res

    while i < len(s) and j < len(s):
        if s[i] == s[j]: 
            curLength += 1
            j += 1
        else: 

            totalHomos += countHomo(j - i)
            i = j
            curLength = 0
    # deal with the current string that needs to be assessed 
    totalHomos += countHomo(j - i)
    return totalHomos % (10**9 + 7)

# Some Tricks below: 

import itertools

# with this, we use the sum of n terms formula ad a trick with itertools.groupby. 
# this effectively trivializes the question to just Time = O(n) and Space = O(1)

def countHomogenous(s):
    countHomos = 0
    for _, group in itertools.groupby(s):
        n = len(list(group))
        countHomos += n*(n + 1) / 2
    return int(countHomos) % (10**9 + 7)



print(countHomogenous("aabbbccccddddd"))

for a, b in itertools.groupby("aabbbccccddddd"): 
    print(a, len(list(b)))

# a 2
# b 3
# c 4
# d 5
# print(list(itertools.groupby("aabbbccccddddd")))