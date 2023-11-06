# kmp-pattern-searching

# Time: O(n); 
# note that as you check at ith place in the txt, and 
# cehcking for m in  pattern, you're also traversing further in txt 
# Space: O(m)
def kmp_search(pat, txt):
    m = len(pat)
    n = len(txt)
    lps = [0]*m
    j = 0           # use j to iterate over pat
    i = 0           # use i to iterate over txt
    computeLPSArray(pat,m,lps)
    while (n-i) >= (m-j): # make sure you have enough chars to check before the end
        if pat[j] == txt[i]: 
            i +=1
            j +=1
        if j == m: 
            print(f'Pattern match at txt index = {i-j}')
            j = lps[j-1]        # reset lps to previous step for more patterns potentially
        elif i < n and pat[j] != txt[i]:
            if j != 0:          # cycle through previous steps to potentially catch more patterns
                j = lps[j-1]
            else: 
                i +=1           # j hits 0; now increment to new i


def computeLPSArray(pat, m, lps): 
    len = 0
    lps[0] = 0      
    i = 1

    while i < m: 
        # if two pointers are equal, the progress and mark the lps[i] = len for coming bakc later 
        if pat[i] == pat[len]:
            len +=1
            lps[i] = len
            i +=1
        else: 
        # for inequality, but you had previous matches, 
            if len != 0:            # len will reset to a previous letter, and i will be continuously checked until len = 0
                len = lps[len - 1]
            else: 
                lps[i] = 0          # at this step it will then assign lps to i, and i will increment
                i +=1


# def computeLPSArray2(pat, m, lps):
#     len = 0
#     lps[0] = 0
#     i = 1

#     while i < m: 
#         if pat[i] == pat[len]:
#             len +=1
#             lps[i] = len
#             i +=1
#         else:
#             if len != 0: 
#                 len = lps[len-1]
#             else: 
#                 lps[i] = 0
#                 i +=1

# -------------------------------------------------- rewrites below -------------------------------------------------- #

def computeLPSArray1(pat, m, lps):
    len = 0
    lps[0] = 0
    i = 1
    while i < m:
        print(i, len, pat[i], pat[len])
        if pat[i] == pat[len]:
            len +=1
            lps[i] = len
            i +=1
        else: 
            if len != 0:
                len = lps[len-1]
            else: 
                lps[i] = 0
                i +=1


def computeLPSArray2(pat, m, lps):
    len = 0
    lps[0] = 0
    i = 0
    while i < m: 
        if pat[i] == pat[len]:
            len +=1
            lps[i] = len
            i +=1
        else: 
            if len !=0:
                len = lps[len-1]
            else: 
                lps[i] = 0
                i +=1



def computeLPSArray3(pat, m, lps):
    len = 0
    lps[0] = 0
    i = 1
    while i < m:   
        if pat[i] == pat[len]: 
            len +=1
            lps[i] = len
            i +=1
        else: 
            if len !=0: 
                len = lps[len-1]
            else: 
                lps[i] = 0
                i +=1

def computeLPSArray4(pat, m, lps):
    len = 0
    lps[0] = 0
    i = 1
    while i < m: 
        if pat[i] == pat[len]: 
            len +=1
            lps[i] = len
            i +=1
        else: 
            if len !=0: 
                len = lps[len-1]
            else: 
                lps[i] = 0
                i +=1







pat = 'ababadb'
m = len(pat)
# print(pat)

lps = [0] * m
computeLPSArray4(pat, m, lps)
print(lps)





txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
kmp_search(pat, txt)