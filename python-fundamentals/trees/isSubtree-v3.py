## isSubtree


## fancy procedure: 
## serialize the trees
## then check if ser_subroot is in ser_root using KMP

# Time: this runs in O(n) for number of nodes in the root (commensurate with KMP)
# Space: O(N) for serializing each root/subroot

def serialize(root):
    if not root: 
        return ',#'
    else: 
        return ',' + str(root.val) + serialize(root.left) + serialize(root.right)

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
            j+=1
        if j == m: 
            return True
        elif i < n and pat[j] != txt[i]:
            if j != 0: 
                j = lps[j-1]
            else: 
                i +=1
    return False

def isSubtree(root, subRoot):
    s_subRoot = serialize(subRoot)
    s_root = serialize(root)
    return kmp_search(s_subRoot, s_root)