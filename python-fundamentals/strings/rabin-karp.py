# Rabin Karp

# q = a prime number
# d = 256 for ord function

pat = 'aba'
txt = 'cvabtabaz'

# this is designed with the hash function

def rabinKarp(pat, txt, q):

    d = 256
    p = 0       # pattern hash value
    t = 0       # txt hash value
    n = len(txt)
    m = len(pat)
    h = 1

    for i in range(m-1):                # h used to cancel the last highest exponential term when iterating using the rolling hash fn
        h = (h*d) % q
        
    for i in range(m):
        p = (d*p + ord(pat[i])) % q     # it's like every iteration, you take the base * last answer mod q 
        t = (d*t + ord(txt[i])) % q

    for s in range(n-m+1):
        if p == t: 
            if pat == txt[s:s+m+1]:
                return s
        if s < n-m: 
            t = (d*(t-ord(txt[s])*h) + ord(txt[s+m])) % q        
            if t < 0:                   # if you have negataive values, just add another q to get to postive
                t = t + q
    return -1



# done without the mod restrictions
# Idea: 
# - Instead of naive approach of checking strings one by one, we build a hash function
#   that maps values of the chars by the base (d) of how mnay chars there are
# - Then if the value of pattern = value of part of string that is tested, we check chars individually
# - if not, we efficiently strip the 'first' char in the string we test, then we bring in the other new value
#   via the "rolling hash function"

# Time: O(N*M) but with the hash function, you decrease worst case chances
# Note with modding, you increase the chances of a sprurious hit (i.e. a false positive of pattern = match)
# but you decrease memory required

# Space: O(1)

def rabinKarp1(pat, txt):

    d = 256
    p = 0       # pattern hash value
    t = 0       # txt hash value
    n = len(txt)
    m = len(pat)
    h = d**(m-1)
        
    for i in range(m):                  # this instantiates the first instance of the rolling hash fn on pattern and text
        p = (d*p + ord(pat[i]))         # it's like every iteration, you take the base * last answer mod q 
        t = (d*t + ord(txt[i]))

    for s in range(n-m+1):
        if p == t: 
            if pat == txt[s:s+m]:
                return s
        if s < n-m: 
            t = (d*(t-ord(txt[s])*h) + ord(txt[s+m]))       # rolling hash function

    return -1


def rabinKarp1(pat, txt):
    d = 256                 # num of chars in hash function
    m = len(pat)
    n = len(txt)
    h = d**(m-1)            # used for undoing the largest base polynomial (i.e. the first letter in the old string in iteration)
    p = 0                   # hash for pat
    t = 0                   # hash for txt

    for i in range(m):                              # instantiate the hash functions on pat and txt for first m chars
        p = (d*p + ord(pat[i]))
        t = (d*t + ord(txt[i]))

    for s in range(n-m+1):                          # traverse through txt on the valid indices 
        if p == t:                                  # hash is equal: check if chars are actually equal
            if pat == txt[s:s+m]:
                return s
        if s < n - m:
            t = d*(t - ord(txt[s])*h) + ord(txt[s+m])   # else: take the largest b^exponent off, then add new term
    return -1



print(rabinKarp1(pat, txt))







#-------------- Crap Below --------------#

















# 123456
# aaaaab
# n = 6

# pattern: 
# m = 3

# 123
# aab
# 112 = 4 = hash code
# /\ hash pattern h(p)

# rolling hash function 


# given codes for all alphabets


# function takes constant time!
# confirm if the chars are equal 


# hash code: for 'abc' = (1)*b^2 + (2)*b^1+(3)*b^0 = z

# rolling hash: (z - (1)*b^2)*b + next*b^0
# base = b

# Time: still O(MN)but reduce the worst case chance significantly

# a = 1
# b = 2
# c = 3
# d = 4
# e = 5
# f = 6
# g

# make the string into a single value instead of checking each individual char
