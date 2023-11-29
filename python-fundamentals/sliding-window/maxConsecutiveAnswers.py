# trivial: if k == num of T or F's, then return len(answerKey)
from itertools import groupby


def maxConsecutiveAnswers(answerKey, k):
    charFreq = []
    curChar = answerKey[0]
    curFreq = 1
    for char in answerKey[1:]:
        if char == curChar: 
            curFreq += 1
        else: 
            charFreq.append([curChar, curFreq])
            curChar = char
            curFreq = 1
    charFreq.append([curChar, curFreq])

    print(charFreq)
    def sWindow(char, tokens):
        left = 0
        right = 0
        counts = 0
        while right < len(charFreq):
            # if curChar == char then add it to counts 
            if charFreq[right][0] == char: 
                counts += charFreq[right][1]
                r += 1
            # decide if you can right -> if you have enough tokens, move it and take it


    # do for both T and F


    # do a groupby 

    # then how do you decide which elements to connect? 


k = 4
answerKey = "TTTFFTTTTFFFTTTFTTFFTTT"
# charFreq = list(groupby(answerKey))[0][1]

print(maxConsecutiveAnswers(answerKey, k))
# dp[i] = max consecutive Ts given dp[i-1]
