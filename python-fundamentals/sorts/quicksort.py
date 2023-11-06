# quicksort
# Time: O(n^2) worst case 


def quicksort(a, p ,r):
    if p < r:
        q = partition(a,p,r)
        quicksort(a,p,q-1)
        quicksort(a,q+1, r)

def partition(a,p,r):
    pivot = a[r]
    i = p - 1
    for j in range(p,r):
        if a[j] <= pivot:
            i+=1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i + 1

# arr = [5,1,7,3,8,4,2,6]
# quicksort(arr, 0, len(arr) - 1)
# print(arr)

# mergesort
def mergesort(a,p,r):
    if p >= r: 
        return 
    q = (p + r)//2
    mergesort(a, p, q)
    mergesort(a, q + 1, r)
    merge(a,p,q,r)

def merge(a,p,q,r):
    left, right = a[p:q+1], a[q+1:r+1]
    lenLeft, lenRight = len(left), len(right)
    i, j, k = 0, 0, p
    while i < lenLeft and j < lenRight:
        if left[i] < right[j]:
            a[k] = left[i]
            i +=1
        else: 
            a[k] = right[j] 
            j +=1
        k +=1
    while i < lenLeft:
        a[k] = left[i]
        i +=1
        k +=1
    while j < lenRight:
        a[k] = right[j] 
        j +=1
        k +=1

# arr = [5,1,7,3,8,4,2,6]

# mergesort(arr, 0, len(arr) - 1)
# print(arr)



### mergesort using different arrays

def mergesort2(arr):
    if len(arr) <= 1:
        return arr
    q = len(arr)//2
    left = mergesort2(arr[:q])
    right = mergesort2(arr[q:])
    return merge2(left, right)

def merge2(left, right):
    lenLeft = len(left)
    lenRight = len(right)
    i, j, k, = 0, 0, 0
    arr = [0] * (lenLeft + lenRight)
    while i < lenLeft and j < lenRight: 
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else: 
            arr[k] = right[j]
            j += 1
        k +=1
    while i < lenLeft:
        arr[k] = left[i]
        i +=1
        k +=1
    while j < lenRight: 
        arr[k] = right[j]
        j +=1
        k +=1
    return arr


# arr = [5,3]
# arr = [5,1,7,3,8,4,2,6]

# x = mergesort2(arr)
# print(x)



def quicksort2(a, p, r):
    if p < r: 
        q = partition2(a, p, r)
        quicksort2(a, p, q-1)
        quicksort2(a,q+1, r)

def partition2(a,p,r):
    pivot = a[r]
    i = p-1
    for j in range(p, r):
        if a[j] <= pivot:
            i +=1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i+1

arr = [5,1,7,3,0,4,2,6]

# quicksort2(arr, 0, len(arr)-1)
# print(arr)

# 
#       k-1
# 01234567 
# |   q  |
# p      r  

def quickselect(a, p, r, k):
    # k > 0 and k < r - p + 1
    # k = 1 means smallest, k = 3 means 3rd smallest, so k'th means k-1 index positions from p
    # index adjusted for position of p between p and r
    if p <= (p + k - 1) <= r:
        q = partition(a,p,r)
        if q == p + k - 1:
            return a[q]
        elif q > p + k - 1: 
            return quickselect(a, p, q-1, k)
        else: 
            # p + (k - 1) - q 
            return quickselect(a, q+1, r, p + (k - 1) - q)
    else: 
        print ("index out of place")

# x = quickselect(arr, 0, 7, 3)
# print(x)


#       'k-1'
# 01234567 
# |   q  |
# p      r  

def quickselectLargest(a,p,r,k):
    if p <= (r - (k -1)) <= r:
        q = partition(a,p,r)
        if q == r - (k-1):
            return a[q]
        elif r-(k-1)  > q: 
            return quickselectLargest(a,q+1,r,k)
        else: 
            return quickselectLargest(a, p, q-1 ,r - (k-1) + q)


y = quickselectLargest(arr, 0, 7, 3)
print(y)