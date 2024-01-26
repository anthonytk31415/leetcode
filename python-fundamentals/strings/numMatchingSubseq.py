
# below is the explanation for KMP but this problem is not a KMP problem since we're not worried about a contiguous substring. 

# when you go to lps[i], you are saying "i and length did not match so i need to traverse back to when there was a common 
# prefix minus 1 so i dont have to go the full way back. and if i get to 0, then i increment i"

def calculateLps(pattern):
    m = len(pattern)
    lps = [0]*m
    i = 1
    length = 0
    while i < m: 
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length 
            i += 1
        else: 
            if length > 0: 
                length = lps[length - 1]
            else: 
                lps[i] = 0
                i += 1
    return lps

pattern = "ababc"
# print(calculateLps(pattern))

# iterate across indices i in text. if text[i] == pattern[j] then we increment i and j. 
# if not, then if j > 0, then we revert j back to its most previous prefix - 1 i.e. j =  lps[j-1]
# otherwise, j =0, no reason to revert, then we increment i.
# Key: the whole point of the longest prefix suffix at i is so we always move forward with i in text
# and if we reach a point when text[i] != pattern[j], then we check at the last point of the prefix
# that we hit a suffix for the next iteration. 

def kmp(pattern, text): 
    lps = calculateLps(pattern)
    m = len(pattern)
    n = len(text)
    i, j = 0, 0
    while i < n: 
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == m: 
                return True
        else: 
            if j > 0: 
                j = lps[j-1]
            else: 
                i += 1

    return False

text = "asdlkfjasdlfkajababcasdf"
# print(kmp(pattern, text))


# this is the naive solution; O(N*M)
def numMatchingSubseq1(s, words):

    index = [0]*len(words)
    res = 0
    for char in s: 
        for i in range(len(index)):
            word = words[i]
            if index[i] < len(words[i]) and char == word[index[i]]:
                index[i] +=1
                if index[i] == len(word): res += 1
    return res

# I had to dig for a solution here. 


from collections import defaultdict
def numMatchingSubseq(s, words):
    buckets = defaultdict(list)
    for word in words: 
        buckets[word[0]].append(word)
    
    res = 0
    for c in s: 
        if c not in buckets: continue 
        oldBucket = [x for x in buckets[c]]
        del buckets[c]
        for word in oldBucket:
            newWord = word[1:]
            if len(newWord) == 0: res += 1
            else: buckets[newWord[0]].append(newWord)
    return res



    
s = "abcde"
words = ["a","bb","acd","ace"]
# s = "dsahjpjauf"
# words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]

# oh i guess you dont have to do KMP, since its not a contiguous string. 
print(numMatchingSubseq(s, words))