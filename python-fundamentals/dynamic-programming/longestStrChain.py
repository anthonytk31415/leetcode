# dp solution
# Sort the words by length and alphabetical order. . 
# We instantiate word candidate, where candidate[n] = {set all words with length n} for easy lookup.
# We also build wordChain[word] = chain of length k
# for each word in words: 
#   - add to candidates for k = length(word) 
#   - for each candidate of k-1 length: if its a valid chain (using isWordChain), keep track of the max chain. 


# for isWordChain, the logic here is if chars are equal then increment i, j, where i, j are indeces in w1, w2. 
# Otherwise, increment errors, and just i. If we get to more than 1 error, return False. 
# If we get to end, return True. 

# Time: O(n*s1*s2): for each word n, we need to check its predecessor s1 with length s2
# Space: O(n): storage for each word its longest chain and the candidates for lenghth k
from collections import defaultdict
def longestStrChain(words):
    def isWordChain(w1, w2):
        i, j, errors = 0, 0, 0
        while i < len(w1) and j < len(w2):
            if w1[i] == w2[j]:
                i += 1
            else: 
                errors += 1
            j += 1
            if errors > 1: return False
        return True

    words.sort(key = lambda x: (len(x), x))
    maxChain = 1
    candidates = defaultdict(set)
    wordChain = {}
    for word in words: 
        candidates[len(word)].add(word)
        curRes = 1
        if candidates[len(word) - 1]:
            for candidate in candidates[len(word) - 1]:
                if isWordChain(candidate, word):
                    curRes = max(wordChain[candidate] + 1, curRes)

        wordChain[word] = curRes
        maxChain = max(maxChain, curRes)        
    return maxChain





# print(isWordChain("xb", "xbc"))
# words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
words = ["a","b","ba","bca","bda","bdca"]
print(longestStrChain(words))