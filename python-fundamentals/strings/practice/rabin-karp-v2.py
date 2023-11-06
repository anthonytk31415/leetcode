# rabin karp


def rabinKarp(pat, txt):
    m = len(pat)
    n = len(txt)
    d = 256                 # base of ord
    h = d**(m-1)            # for rolling hash map
    hash_p = 0
    hash_t = 0
    for i in range(m):
        hash_p = d*hash_p + ord(pat[i])
        hash_t = d*hash_t + ord(txt[i])
    for j in range(n-m+1):
        if hash_p == hash_t: 
            if pat == txt[j:j+m]:
                print(f'Patern detected at index {j}')
        if j < n-m:
            hash_t = d*(hash_t - ord(txt[j])*h) + ord(txt[j+m])



def rabinKarp2(pat, txt):
    m = len(pat)
    n = len(txt)
    d = 256
    h = d**(m-1)
    hash_p = 0
    hash_t = 0
    for i in range(m):
        hash_p = d*hash_p + ord(pat[i])
        hash_t = d*hash_t + ord(txt[i])
    
    for s in range(n-m+1):
        if hash_p == hash_t: 
            if pat == txt[s:s+m]:
                print(f'pattern detected at index: {s}')
        if s < n-m:                                         # dont evalulate to pop a crappy answer if you're past n-m
            hash_t = d*(hash_t - h*ord(txt[s])) + ord(txt[s+m])


def rabinKarp3(pat, txt):
    d = 256
    m = len(pat)
    n = len(txt)
    h = d**(m-1)
    hash_p = 0
    hash_t = 0
    for i in range(len(pat)):
        hash_p = d*hash_p + ord(pat[i])
        hash_t = d*hash_t + ord(txt[i])
    
    for s in range(n-m+1):
        if hash_p == hash_t: 
            if pat == txt[s:s+m]:
                print(f'Pattern recognized at index: {s}')
        if s < n-m: 
            hash_t = d*(hash_t - h*ord(txt[s])) + ord(txt[s+m])

pat = 'aba'
txt = 'cvabtabaz'

rabinKarp3(pat, txt)