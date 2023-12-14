# kind of a sliding window problem. 

# s1Elements = contains count of s1 characters

# # start with window of len(s1). 
# notInS1

# for each traversal, if it's in s1, subtract it. if it hits 0, delete it. if 

# if its not in s1, 
from collections import Counter

def checkInclusion(s1, s2):
    s1Tracker = Counter(s1)
    inS1 = Counter()
    notInS1 = Counter()

    for i in range(len(s1)):
        if s2[i] in s1Tracker: 
            inS1[s2[i]] +=1
            s1Tracker[s2[i]] -=1
            if s1Tracker[s2[i]] == 0: del s1Tracker[s2[i]]
        else: 
            notInS1[s2[i]] += 1
    if not s1Tracker: 
        return True

    print(s1Tracker, inS1, notInS1)
    for i in range (len(s1), len(s2)):
        left = i - len(s1)
        if s2[left] in notInS1: 
            notInS1[s2[left]] -=1
            if notInS1[s2[left]] == 0: del notInS1[s2[left]]
        else: 
            inS1[s2[left]] -=1
            s1Tracker[s2[left]] += 1

        if s2[i] in s1Tracker: 
            inS1[s2[i]] +=1
            s1Tracker[s2[i]] -=1
            if s1Tracker[s2[i]] == 0: del s1Tracker[s2[i]]
        else: 
            notInS1[s2[i]] += 1
        print(s1Tracker, inS1, notInS1, "i: ", i, s2[i])
        if not s1Tracker: 
            return True
    return False


s1 = "abc"
s2 = "cccccbbbbaaaa"
print(checkInclusion(s1, s2))