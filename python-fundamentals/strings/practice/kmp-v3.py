def lpsArray(pat, m, lps):
    len = 0
    lps[0] = 0
    i = 1
    while i < m: 
        if pat[len] == pat[i]: 
            len +=1
            lps[i] = len
            i +=1
        else: 
            if len != 0: 
                len = lps[len-1]
            else: 
                lps[i] = 0
                i +=1
    
def kmp_search(pat, txt):
    m = len(pat)
    n = len(txt)
    lps = [0]*m
    lpsArray(pat, m, lps)
    i = 0
    j = 0
    while (n - i) >= (m - j):
        if pat[j] == txt[i]:
            i +=1
            j +=1
        if j == m: 
            print(f'Pattern recognized at {i-j}')
            j = lps[j-1]
        elif i < n and pat[j] != txt[i]:
            if j !=0: 
                j = lps[j-1]
            else: 
                i +=1

txt = 'abacabbabb'
pat = 'abb'
kmp_search(pat, txt)
