## kmp rewrites 



# def lpsArray(pat, m, lps):
#     len = 0
#     lps[0] = 0
#     i = 1
#     while i < m: 
#         if pat[i] == pat[len]:
#             len +=1
#             lps[i] = len
#             i +=1
#         else: 
#             if len !=0:
#                 len = lps[len-1]
#             else: 
#                 lps[i] = 0
#                 i +=1

# def kmp_search(pat, txt):
#     m = len(pat)
#     n = len(txt)
#     lps = [0]*m
#     lpsArray(pat, m, lps)

#     i = 0       # txt
#     j = 0       # pat

#     while (n - i) >= (m - j):
#         if pat[j] == txt[i]:
#             i +=1
#             j +=1
#         if j == m: 
#             print(f'pattern recognized at {i - j}')
#             j = lps[j-1]
#         elif i < n and pat[j] != txt[i]:
#             if j != 0: 
#                 j = lps[j-1]
#             else: 
#                 i +=1



# def lpsArray(pat, m, lps):
#     len = 0
#     lps[0] = 0
#     i = 1
#     while i < m: 
#         if pat[i] == pat[len]:
#             len +=1
#             lps[i] = len
#             i +=1
#         else: 
#             if len !=0: 
#                 len = lps[len-1]
#             else: 
#                 lps[i] = 0
#                 i +=1

# def kmp_search(pat, txt):
#     m = len(pat)
#     n = len(txt)
#     lps = [0] * m
#     i = 0
#     j = 0
#     lpsArray(pat, m, lps)
#     while (n - i) >= (m - j): 
#         if pat[j] == txt[i]: 
#             i +=1
#             j +=1
#         if j == m:
#             print(f'pattern detected at {i-j}')
#             j = lps[j-1]
#         elif i < n and pat[j] != txt[i]:        # ensure you have more room to increment i while checking pattern
#             if j !=0: 
#                 j = lps[j-1]
#             else: 
#                 i +=1


# def lpsArray(pat, m, lps):
#     len = 0
#     lps[0] = 0
#     i = 1
#     while i < m: 
#         if pat[i] == pat[len]:
#             len +=1
#             lps[i] = len
#             i +=1
#         else: 
#             if len !=0: 
#                 len = lps[len-1]
#             else: 
#                 lps[i]=0
#                 i +=1

# def kmp_search(pat, txt):
#     m = len(pat)
#     n = len(txt)
#     lps = [0]*m
#     lpsArray(pat, m, lps)
#     i = 0
#     j = 0

#     while (n - i) >= (m - j):
#         if pat[j] == txt[i]:
#             i +=1
#             j +=1
#         if j == m: 
#             print(f'pattern reached at {i-j}')
#             j = lps[j-1]
#         elif i < n and pat[j] != txt[i]: 
#             if j !=0: 
#                 j = lps[j-1]
#             else: 
#                 i +=1




# def lpsArray(pat, m, lps):
#     len = 0
#     lps[0] = 0
#     i = 1
#     while i < m:
#         if pat[i] == pat[len]:
#             len +=1
#             lps[i] = len
#             i +=1
#         else: 
#             if len !=0: 
#                 len = lps[len-1]
#             else: 
#                 lps[i] = 0
#                 i +=1

# def kmp_search(pat, txt):
#     m = len(pat)
#     n = len(txt)
#     lps = [0]*m
#     lpsArray(pat, m, lps)
#     i = 0
#     j = 0
#     while (n - i) >= (m-j):
#         if pat[j] == txt[i]:
#             i +=1
#             j +=1
#         if j == m: 
#             print(f'pattern at {i-j}')
#             j = lps[j-1]
#         elif i < n and pat[j] != txt[i]:
#             if j !=0: 
#                 j = lps[j-1]
#             else: 
#                 i +=1


def lpsArray(pat, m, lps):
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

def kmp_search(pat , txt):
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
            print(f'Pattern detected at {i-j}')
            j = lps[j-1]
        elif i < n and pat[j] != txt[i]:
            if j !=0: 
                j = lps[j-1]
            else: 
                i +=1
        

txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
kmp_search(pat, txt)
# expected: pattern detected at 10