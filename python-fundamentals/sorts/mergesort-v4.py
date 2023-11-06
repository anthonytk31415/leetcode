def insertionsort(a):
    for i in range(1,len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j+1] = a[j]
            j -=1
        a[j+1] = key


def mergesort(a,p,r):
    if p >= r:
        return
    q = (r + p) // 2
    mergesort(a, p, q)
    mergesort(a, q+1, r)
    merge(a,p,q,r)

def merge(a,p,q,r):
    len_l = q - p + 1
    len_r = r - (q + 1) + 1
    left = a[p:q+1]
    right = a[q+1:r+1]
    i = 0
    j = 0
    k = p
    while i < len_l and j < len_r:
        if left[i] < right[j]:
            a[k] = left[i]
            i +=1
        else: 
            a[k] = right[j]
            j +=1
        k +=1
    while i < len_l:
        a[k] = left[i]
        i +=1
        k +=1
    while j < len_r: 
        a[k] = right[j]
        j +=1
        k +=1

a = [4,1,6,7,3,8,2,5]
print(mergesort(a, 0, 7))
print(a)