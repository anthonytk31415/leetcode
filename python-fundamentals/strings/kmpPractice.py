# KMP algorithm


def computeLpsArray(pattern):
    m = len(pattern)
    lps = [0]*m
    length = 0
    i = 1

    while i < m: 
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
    n = len(text)
    m = len(pattern)
    lps = computeLpsArray(pattern)
    i, j = 0,0
    indices = []
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
            if j == m:                 
                indices.append(i-j)
                j = lps[j - 1]
        else: 
            if j != 0: 
                j = lps[j-1]
            else: 
                i += 1
    return indices




# def calcLps(pattern):










pattern = "ababaca"
#          0012301
print(computeLpsArray(pattern))

text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
result = kmp(text, pattern)
print("Pattern found at indices:", result)