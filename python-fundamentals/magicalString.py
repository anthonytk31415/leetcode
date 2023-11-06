# Time: O(n)
# Space: O(n)


# the loop: 
# - take the string, then build b
# - then build the pairs in a
# - then rebuild the string 

def magicalString2(n):

    s = '1221121221221121122'
    a = []
    b = []
    i, j = 0, 0           # will be one more than then length of i
    while len(s) < n:

        # build b: 
        for idx_j in range(j, len(s)):
            b.append(s[idx_j])
            j +=1
        ## build a-array cycle
        while len(a) < len(b):
            for idx in range(i, j):
                if idx % 2 == 0: 
                    char = '1'
                else: 
                    char = '2' 
                a.append(char * int(b[idx]))
            i = j
        # build the s string
        s = ''.join(a)
    counter = 0
    for t in range(0, n):
        if s[t] == '1': 
            counter +=1
    return counter

# print(magicalString2(6))
n = 9758
print(magicalString2(n))