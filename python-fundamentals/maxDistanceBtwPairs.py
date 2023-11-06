#two p
# ointers problem, linear solution


def maxDistance(nums1, nums2):
    delta = 0
    i = 0
    j = 0
    while 0 <= i < len(nums1) and 0 <= j < len(nums2):

        if nums1[i] <= nums2[j]:
            delta = max(delta, j - i)
            j +=1
        else: 
            i +=1
            j +=1
    return delta

# nums1 = [55,30,5,4,2]
# nums2 = [100,20,10,10,5]
# nums1 = [2,2,2]
# nums2 = [10,10,1]
nums1 = [30,29,19,5]
nums2 = [25,25,25,25,25]
print(maxDistance(nums1, nums2))