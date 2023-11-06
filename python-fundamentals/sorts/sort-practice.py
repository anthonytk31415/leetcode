def quicksort(a,p,r):
    if p < r:
        q = partition(a,p,r)
        quicksort(a, p, q-1)
        quicksort(a,q+1, r)

def partition(a,p,r):
    pivot = a[r]
    i = p - 1
    for j in range(p,r):
        if a[j]<= pivot:
            i +=1
            a[j], a[i] = a[i], a[j]
    a[i+1], a[r] = a[r], a[i+1]
    return i + 1


arr = [1,3,2,0,4,6,7,5]
# quicksort(arr, 0, 7)
# print(arr)

def quickselect(a,p,r,k):
    if p <= p + (k - 1) <= r:
        q = partition(a,p,r)
        if q == p + (k - 1):
            return a[q]
        if q > p + (k - 1):
            return quickselect(a,p,q-1, k)
        else:
            return quickselect(a,q+1, r, p + (k-1) - q)
    else:
        print('index out of range :(')

print(quickselect(arr, 0, 7,3))

def mergesort(a,p,r):
    if p >= r:
        return
    q = (p + r)//2
    mergesort(a,p,q)
    mergesort(a,q+1,r)
    merge(a,p,q,r)

def merge(a,p,r):
    left = 
    right = 
