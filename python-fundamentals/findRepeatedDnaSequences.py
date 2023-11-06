from collections import defaultdict
# Time: O(n) for running through the string of length n 
# Space: O(n) for storing n sequences of length 10

def findRepeatedDnaSequences(s):
    res = []
    if len(s) < 10: 
        return res
    
    seq = defaultdict(int)
    
    word = s[:10]
    seq[word] +=1
    print(word)
    for i in range(10, len(s)):
        word = word[1:] + s[i]
        seq[word] +=1
        # print(word, i)
        if seq[word] ==2: 
            res.append(word)
    
    # print(seq)
    return res

s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

print(findRepeatedDnaSequences(s))