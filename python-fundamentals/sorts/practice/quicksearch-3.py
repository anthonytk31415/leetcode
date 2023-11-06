# quicksort


def quicksort(a,p,r):
    if p < r: 
        q = partition(a,p,r)
        quicksort(a,p,q-1)
        quicksort(a,q+1, r)

def partition(a,p,r):
    pivot = a[r]
    i = p-1
    for j in range(p,r):
        if a[j] < pivot: 
            i +=1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i + 1

# z = [0,4,5,2,7,3,6,1]
# quicksort(z,0,7)
# print(z)


def quickselect(a,p,r,k):
    if p <= p + k - 1 <= r: 
        q = partition(a,p,r)
        if q == p + (k - 1):
            return q
        elif q > p + (k - 1):
            return quickselect(a,p,q-1, k)
        else: 
            return quickselect(a,q+1, r, p + (k-1) - q)


z = [0,4,5,2,7,3,6,1]
a = quickselect(z,0,7,1)
print(z)
print(a)


