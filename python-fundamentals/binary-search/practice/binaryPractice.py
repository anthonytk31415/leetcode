



def binarySearch(arr, val):
    

    p = 0
    r = len(arr) - 1
    while p < r: 
        q = (p + r) //2 
        print(p, r, q)
        if arr[q] == val: 
            return q
        if arr[q] < val: 
            p = q + 1
        else: 
            r = q - 1
    print(p, r)
    if arr[p] == val: 
        return p
    else: 
        return -1


arr = [0,1,2,2.5,4,5,6,7]
val = 3
print(binarySearch(arr, val))