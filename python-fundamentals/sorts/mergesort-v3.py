## mergesort


# def mergesort(a, p, r):
#     print(a[p:r+1])
#     if p >= r:
#         return
#     q = (p + r) // 2
#     mergesort(a, p ,q)
#     mergesort(a, q+1, r)
#     merge(a,p,q,r)


# def merge(a, p, q, r):
#     len_l = q - p + 1
#     len_r = r - (q + 1) + 1
#     left = [x for x in a[p:q+1]]
#     right = [x for x in a[q+1:r+1]]
#     print(left, right)
#     print(len_l, len_r)
#     i = 0
#     j = 0
#     k = p
    
#     while i < len_l and j < len_r: 
#         if left[i] < right[j]:
#             a[k] = left[i]
#             i +=1
#         else: 
#             a[k] = right[j]
#             j +=1
#         k += 1
#     while i < len_l:
#         a[k] = left[i]
#         i +=1
#         k +=1
#     while j < len_r:
#         a[k] = right[j]
#         j +=1
#         k +=1
#     print(a[p:r+1])





# p = 0
# r = 3
# q = (p + r) // 2
# print(p, q, r)
# left = [x for x in a[p:q+1]]
# print(left)
# right = [x for x in a[q+1:r+1]]
# print(right)


def mergesort(a,p,r):
    if p >=r: 
        return
    q = (p + q) // 2
    mergesort(a, p, q)
    mergesort(a, q+1, r)
    merge(a,p,q,r)


def merge(a,p,q,r):
    len_l = q - p + 1
    len_r = r - (q + 1) + 1
    left = [x for x in a[p:q+1]]
    right = [x for x in a[q+1:r+1]]
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

a = [4,1,6,7]
# mergesort(a, 0, 3)
# print(a)
a = [4,1,6,7,3,8,2,5]
mergesort(a, 0, 7)