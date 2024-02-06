def minimumTimeToInitialState1(word, k):
    seconds = 1
    wordStart = k      ## with each iteration, increment by k
    wordLimit = len(word) - k   ## each iteration, decrement by k
    j = 0
    while wordStart < len(word): 

        for i in range(wordStart, len(word)):

            if word[i] == word[j]:
                j += 1
                if j >= wordLimit: return seconds
            else: 
                seconds += 1
                wordStart += k
                wordLimit -= k
                j = 0
                break 

    return seconds



def minimumTimeToInitialState(word, k):
    def computeLps(pattern):
        lps = [0]*len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length > 0:
                    length = lps[length-1]
                else: 
                    lps[i] = 0
                    i += 1
        return lps 

    lps = computeLps(word)
    # print(lps)    kl  kl     asdfghuijop[]
    seconds = 1
    wordStart = k      ## with each iteration, increment by k
    wordLimit = len(word) - k   ## each iteration, decrement by k
    i = wordStart
    j = 0
    while i < len(word):  
        print(i, j, word[i], word[j], wordStart, wordLimit)
        if word[i] == word[j]:
            i += 1
            j += 1
            if j >= wordLimit: 
                print(i, j, "this is triggered")
                return seconds
        else: 
            if j > 0: 
                j = lps[j - 1]
            else: 
                seconds += 1
                wordStart += k
                wordLimit -= k
                i = wordStart

    print(i, j, wordStart)
    return seconds



word = "abaa"
k = 1

# baa*
# aa**
# word = "abacaba"
# k = 3
                 
# word = "abacaba"
# k = 3

# word = "abacaba"
# k = 4

# word = "abcbabcd"
# k = 2

print(minimumTimeToInitialState(word, k))