## mergesort
import math

def merge(a, p, q, r):
    # print('calling merge')
    # print(a)
    # print('{0}, {1}, {2}'.format(p,q,r))
    len_left = q - p + 1
    len_right = r - q 
    # make the left and right copies of a
    # print('coordinates - [{0},{1}]; [{2}, {3}]'.format(p,q,q+1,r))
    # print('left {0}, right {1}'.format(len_left, len_right))
    left = a[p: q+1] # don't forget the indeces don't include the end, so you add one
    right = a[q+1: r+1] 
    # print(left)
    # print(right)
    i = 0
    j = 0
    k = p
    while i < len_left and j < len_right:
        if left[i] <= right[j]:
            a[k] = left[i]
            i = i + 1
        else:
            a[k] =  right[j]
            j = j + 1
        k = k + 1
    while i < len_left:
        a[k] = left[i]
        i = i + 1
        k = k + 1
    while j < len_right:
        a[k] = right[j]
        j = j + 1
        k = k + 1
    # print(a)

def mergesort(a, p, r):
    if p >= r:
        return 
    q = math.floor( (p + r)/2 )
    print(q)
    mergesort(a, p, q)
    mergesort(a, q+1, r)
    merge(a, p, q, r)




# z = [23,10]
# z = [23,10,1,5,89,3,15,24]
# z1 = mergesort(z, 0, 7)
# mergesort(z,0,1)