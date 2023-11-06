# longestcommonprefix

def longestCommonPrefix(strs):
    if len(strs) == 1: 
        return strs[0]
    check = strs[0]
    strs = strs[1:]
    for i in range(len(check)):
        if not all([check[i] == x[i] if i < len(x) else False for x in strs ]):
            return check[:i+1]
    return check