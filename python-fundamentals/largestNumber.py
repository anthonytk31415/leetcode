
def mergesort(a,p,r):
    if p >= r: 
        return 
    else: 
        q = (r + p) // 2
        mergesort(a,p,q)
        mergesort(a,q+1, r)
        merge(a,p,q,r)

def merge(a,p,q,r):
    left = a[p:q+1]
    right = a[q+1: r+1]
    k = p
    i,j = 0,0
    while i < len(left) and j < len(right):        
        if str(left[i]) + str(right[j]) > str(right[j]) + str(left[i]):
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


def largestNumber(nums):
    mergesort(nums, 0, len(nums)-1)
    res = ''
    for x in nums: 
        res = res + str(x)
    return str(int(res))

import functools 

def mysort(nums):
    nums.sort(key = functools.cmp_to_key(lambda x, y: -(int(str(x) + str(y)) - int(str(y) + str(x)))))
    res = ''
    for x in nums: 
        res = res + str(x)
    return str(int(res))

nums = [3,30,34,5,9]
print(mysort(nums))
