### rabin karp



def rabinKarp(pat, txt):
    d = 256
    m = len(pat)
    n = len(txt)
    h = d**(m-1)
    hash_p = 0
    hash_t = 0
    
    for i in range(m):
        hash_p = d*hash_p + ord(pat[i])
        hash_t = d*hash_t + ord(txt[i])
    
    for s in range(n - m + 1):
        if hash_p == hash_t: 
            if pat == txt[s:s+m]:
                print(f'pattern detected at {s}')
        if s < n-m: 
                hash_t = d*(hash_t - h*ord(txt[s])) + ord(txt[s+m])

txt = 'anthony'
pat = 'ny'
rabinKarp(pat, txt)