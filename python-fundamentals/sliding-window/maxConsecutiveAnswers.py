# trivial: if k == num of T or F's, then return len(answerKey)
# from itertools import groupby

#     charFreq = []
#     curChar = answerKey[0]
#     curFreq = 1
#     for char in answerKey[1:]:
#         if char == curChar: 
#             curFreq += 1
#         else: 
#             charFreq.append([curChar, curFreq])
#             curChar = char
#             curFreq = 1
#     charFreq.append([curChar, curFreq])


def maxConsecutiveAnswers(answerKey, k):

    def slidingWindow(char, tokens):
        left, counts, maxCount = 0, 0, 0
        
        for right in answerKey: 
            if right != char: 
                if tokens == 0: 
                    while answerKey[left] == char: 
                        left += 1
                        counts -= 1
                    if answerKey[left] != char:
                        tokens += 1
                        left += 1
                        counts -=1
                if tokens > 0: 
                    tokens -= 1
            # if we're not at char, we have already bought a token to take current; 
            counts += 1
            maxCount = max(maxCount, counts)
        return maxCount

    # print((slidingWindow("T", k), slidingWindow("F", k)))
    return max(slidingWindow("T", k), slidingWindow("F", k))
        

from itertools import accumulate
arr = [1,2,3,4,5]
prefixSum = list(accumulate(arr))
print(prefixSum)
# >> [1, 3, 6, 10, 15]


k = 2
# answerKey = "TTFFTTF"
# answerKey = "TTTFFTTTTFFFTTT"
answerKey = "TTTFTTFFTTT"
# charFreq = list(groupby(answerKey))[0][1]

print(maxConsecutiveAnswers(answerKey, k))
# dp[i] = max consecutive Ts given dp[i-1]
