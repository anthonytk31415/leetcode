


def computeLps(pattern):
    length = 0
    i = 1
    lps = [0]*len(pattern)

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else: 
            if length != 0:
                length = lps[length - 1]
            else: 
                lps[i] = 0
                i += 1
    return lps


def kmp(text, pattern):
    lps = computeLps(pattern)
    i,j = 0, 0
    res = []
    while i < len(text):

        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                res.append(i-len(pattern))
                j = lps[j-1]
        else: 
            if j != 0: 
                j = lps[j-1]
            else:                 
                i += 1
    return res


def beautifulIndices(s, a, b, k):
    aIdx = kmp(s, a)
    bIdx = kmp(s, b)
    print(aIdx, bIdx)
    res = []
    j = 0
    for i in range(len(aIdx)):
        while j < len(bIdx) and bIdx[j] < aIdx[i] - k: 
            j += 1

        if j < len(bIdx) and abs(bIdx[j] - aIdx[i]) <= k: 
            res.append(aIdx[i])

    return res


s = "isawsquirrelnearmysquirrelhouseohmy"
a = "my"
b = "squirrel"
k = 15

print(beautifulIndices(s,a,b,k))


pattern = "ababaca"
#          0012301
# print(computeLps(pattern))

text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
result = kmp(text, pattern)
print("Pattern found at indices:", result)