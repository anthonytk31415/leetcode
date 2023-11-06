# binarysearch


def binarysearch(a, p, r, key):
    if p >r:
            return -1
    if p == r: 
        if a[p] == key: 
            return p 
        else: 
            return -1
    q = (p + r)// 2
    if a[q] == key: 
        return q
    elif key < a[q]: 
        return binarysearch(a,p, q-1, key)
    else: 
        return binarysearch(a,q+1, r, key)


a = [1,3,5,7,8]
print(binarysearch(a, 0,4,4))