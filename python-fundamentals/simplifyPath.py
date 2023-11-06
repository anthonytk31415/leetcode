from collections import deque
def simplifyPath(path):
    arr = path.split('/')
    res = []
    for i, x in enumerate(arr): 
        if x == '' or x == '.': 
            continue 
        if x == '..':
            if res: res.pop()
        else: 
            res.append(x)
    return '/' + '/'.join(res)

# str = "/home//foo/"
# str = "/home/"
path = "/a/./b/../../c/"
print(simplifyPath(path))