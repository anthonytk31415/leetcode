def mergesort(arr):
    if len(arr) == 0: return None
    if len(arr) == 1: return arr
    mid = (len(arr) - 1)//2
    left = mergesort(arr[:mid+1])
    right = mergesort(arr[mid + 1:])
    return merge(left, right)

def merge(a, b):
    i, j, k, res = 0, 0, 0, [None]*(len(a) + len(b))
    while i < len(a) and j < len(b):
        if a[i] < b[j]: 
            res[k] = a[i]
            i += 1
        else: 
            res[k] = b[j]
            j += 1
        k += 1
    while i < len(a): 
        res[k] = a[i]
        i += 1
        k += 1
    while j < len(b):
        res[k] = b[j]
        j += 1
        k += 1
    return res


arr = [7,3,1,0,6,5,4,2]
print(mergesort(arr))