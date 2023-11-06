

def quicksort(a,p,r):
    if p < r:
        q = partition(a,p,r)
        quicksort(a,p,q-1)
        quicksort(a,q+1, r)

def partition(a,p,r):
    pivot = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= pivot: 
            i +=1
            a[j], a[i] = a[i], a[j]
    a[i+1], a[r] = a[r], a[i+1]
    return i + 1

# arr = [5,2,6,8,1,3,4,7]

# quicksort(arr, 0, 7)
# print(arr)

def mergesort(a,p,r):
    if p >= r: 
        return 
    q = (p + r) //2
    mergesort(a,p,q)
    mergesort(a,q+1,r)
    merge(a, p,q,r)

def merge(a,p,q,r):
    left = a[p:q+1]
    right = a[q+1:r+1]
    i, j, k = 0, 0, p
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            a[k] = left[i]
            i +=1
        else:
            a[k] = right[j]
            j +=1        
        k +=1
    while i < len(left):
        a[k] = left[i]
        i +=1
        k +=1
    while j < len(right):
        a[k] = right[j]
        j +=1
        k +=1

arr = [5,2,6,8,1,3,4,7]
mergesort(arr, 0, 7)
print(arr)