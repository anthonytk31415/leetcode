

def binarySearch(a, target, p, r):
    print(p, r)
    if p >= r: 
        if p == r and a[p] == target: 
            return True
        else: 
            return False    
    q = (p + r) // 2
    if a[q] == target: 
        return True
    elif a[q] < target: 
        return binarySearch(a, target, q+1, r)
    else: 
        return binarySearch(a, target, p, q-1)

a = [0,1,2,3,4,5,6,7,8,9,11]
target = -13
print(binarySearch(a, target, 0, len(a)-1))