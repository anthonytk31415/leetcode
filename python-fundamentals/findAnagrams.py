# findAnagrams

# create a lookup that contains occurance of letters in p
# then you'll check on string s starting with index = 0 to len(p) - 1 (leavig the last) letter to check for iteration into the templookup
# then the iteration is as follows: 
# - from len(p)-1 to the end of len(s):
# - add s[i] into tempLookup
# - if s[i] in lookup --> if lookup == tempLookup, then append the index of the first letter (i - (len(p)- 1))
# - now remove the 'first' letter of the checked string from tempLookup: this is at index i - len(p) + 1
# - note quirks to check equal dictionaries: you dont want zeroes,  you want to delete the letter if the count brings the entry from 1 to 0


def findAnagrams(s, p):
    if len(p) > len(s):
        return []
    lookup = {}
    res = []
    for x in p: 
        if x not in lookup:
            lookup[x]=1
        else: 
            lookup[x] += 1

    tempLookup = {}
    for i in range(0,len(p)-1):
        cur = s[i]
        if cur not in tempLookup:
            tempLookup[cur] = 1
        else: 
            tempLookup[cur] +=1

    for i in range(len(p)-1, len(s)):
        toRemove = s[i-(len(p)-1)]
        cur = s[i]
        # add new entry into the templookup
        if cur in tempLookup:
            tempLookup[cur] +=1
        else: 
            tempLookup[cur] = 1
        # check if temp lookup = lookup
        # print(lookup, tempLookup)
        if cur in lookup:
            if tempLookup == lookup:
                res.append(i - len(p)+1)
        # remove the 'first part of the checked string to make room for the next iteration
        if tempLookup[toRemove] == 1:
            del tempLookup[toRemove]
        else: 
            tempLookup[toRemove] -=1
    return res

print(findAnagrams('aaaaaaaaaaaa', 'aa'))