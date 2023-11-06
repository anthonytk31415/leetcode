# ab
# 01
# ababc
# 01234
# OOxxx
# from 0 to len(n) - len(m) + 1
# 

def rabinKarp(pat, txt):
    m = len(pat)
    n = len(txt)
    d = 256
    h = d**(m-1)        # up to m - 1 times for max exponent
    txt_val = 0
    pat_val = 0
    for i in range(m):
        pat_val = pat_val*d + ord(pat[i])
        txt_val = txt_val*d + ord(txt[i])

    # if the values are equal, print where it occurs 
    # iterate from 
    j = m
    while j <= n:
        if pat_val == txt_val and pat == txt[j-m:j]:
            print(f'match found at {j - m}')

        if j < n: 
            txt_val = (txt_val - ord(txt[j-m])*h) * d + ord(txt[j])
        j +=1

pat = 'ab'
txt = 'ababc'

rabinKarp(pat, txt)

    

# KMP 



