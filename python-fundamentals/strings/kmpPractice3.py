def computeLps(pattern):
    lps = [0]*len(pattern)
    i = 1
    length = 0

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
    i = 0
    j = 0
    res = []
    while i < len(text):
        if text[i] == pattern[j]:
            i +=1
            j += 1
            if j == len(pattern):
                res.append(i-j)
                j = lps[j-1]
        else: 
            if j > 0: 
                j = lps[j-1]
            else: 
                i += 1

    return res



pattern = "ababaca"
#          0012301
print(computeLps(pattern))

text = "ABABDABACDABABCABABCABAB"
pattern = "ABABCABAB"
# res: [10, 15] (expected)
result = kmp(text, pattern)
print("Pattern found at indices:", result)
