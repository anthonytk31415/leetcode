# median of two sorted arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays/



## merge the two using "merge"
## then take the median


def merge(a, b):
    c = [0]*(len(a)+len(b))
    i = 0
    j = 0
    k = 0
    while i < len(a) and j < len(b): 
        if a[i] < b[j]:
            c[k] = a[i]
            i +=1
        else: 
            c[k] = b[j]
            j +=1   
        k +=1
    while i < len(a):
        c[k] = a[i]
        i +=1
        k +=1   
    while j < len(b):
        c[k] = b[j]
        j +=1
        k +=1   
    return c 
    
def findMedianSortedArrays(nums1, nums2):
    merged = merge(nums1, nums2)
    median = len(merged) //2
    if len(merged) % 2 == 1:
        return merged[median]
    else: 
        return (merged[median] + merged[median-1])/2


