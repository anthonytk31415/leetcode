def quicksort(a,p,r):
    if p < r: 
        q = partition(a,p,r)
        quicksort(a,p,q-1)
        quicksort(a,q+1,r)

def partition(a,p,r):
    pivot = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] < pivot: 
            i +=1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[r] = a[r], a[i+1]
    return i + 1
     
# a = [7,0,4,3,5,1,2,6, 8,-1]
# quicksort(a, 0, 7)



def quickselect(a,p,r,k):
    if p <= p + (k-1) <= r:
        q = partition(a,p,r)
        if q == p + (k-1):
            return a[q]
        if q > p + (k-1):
            return quickselect(a, p, q-1, k)
        else: 
            return quickselect(a, q+1, r, p + (k-1) - q)

# a = [7,0,4,3,5,1,2,6, 8,-1]
# quicksort(a,0,len(a)-1)

# b = quickselect(a,0,len(a)-1,3)
# print(b)
# print(a)

def mergesort(a,p,r):
    if p >=r: 
        return 
    q = (r + p)//2
    mergesort(a,p,q)
    mergesort(a,q+1,r)
    merge(a,p,q,r)

def merge(a,p,q,r):
    left = a[p:q+1]
    right = a[q+1:r+1]
    i,j,k = 0,0,p
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

a = [7,0,4,3,5,1,2,6, 8,-1]
mergesort(a,0,len(a)-1)
print(a)


