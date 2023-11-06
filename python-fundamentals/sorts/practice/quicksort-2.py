# quicksort

def quicksort(a,p,r):
    if p < r: 
        q = partition(a,p,r)
        quicksort(a, p, q-1)
        quicksort(a, q+1, r)

def partition(a,p,r):
    pivot = a[r]
    i = p - 1
    for j in range(p,r):
        if a[j] < pivot:
            i +=1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i + 1


a = [5,3,7,8,1,6,2,4]

# quicksort(a,0,7)
# print(a)

# average time: O(n); worst case: O(n^2)
# space: O(1)
def quickselect(a,p,r, k):
    if p <= p + (k-1) <= r:
        q = partition(a,p,r)
        if q == p + (k-1):
            return a[p+k-1]
        elif q > p + k - 1:
            return quickselect(a,p,q-1, k)
        else: 
            return quickselect(a,q+1,r, p + k -1 -q)

z = quickselect(a,0,7,3)
print(z)