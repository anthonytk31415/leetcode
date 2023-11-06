# merge


def merge(nums1, m, nums2, n):

    left = [0]*m
    for i in range(m):
        left[i] = nums1[i]        
    i = j = k = 0
    while i < m and j < n: 
        print(i,j,k)
        if left[i] < nums2[j]:
            nums1[k] = left[i]
            i +=1
        else: 
            nums1[k] = nums2[j]
            j +=1
        k +=1
    while i < m:
        nums1[k] = left[i]
        i +=1
        k +=1
    while j < n: 
        nums1[k] = nums2[j]
        j +=1
        k +=1

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

merge(nums1, 3, nums2, 3)
print(nums1)