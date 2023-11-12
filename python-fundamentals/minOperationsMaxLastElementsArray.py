#https://leetcode.com/contest/weekly-contest-371/problems/minimum-operations-to-maximize-last-elements-in-arrays/

def minOperations(nums1, nums2):
    
    swaps0 = 0
    # check min swaps by changing before max element
    for i in range(len(nums1)-1):
        n1, n2 = nums1[i], nums2[i]
        if n1 > nums1[-1] and n1 > nums2[-1] and n2 > nums1[-1] and n2 > nums2[-1]:
            return -1
        # n1 and n2 are greater than some max
        elif (n1 > nums1[-1] and n2 > nums1[-1] ) or (n1 > nums2[-1] and n2 > nums2[-1] ):
            return -1 
        elif n1 <= nums1[-1] and n2 <= nums2[-1]: 
            # print(n1, n2, nums1[-1], nums2[-1])
            continue
        elif (n1 > nums1[-1] and n1 <= nums2[-1] ) or (n2 > nums2[-1] and n2 <= nums1[-1]): 
            # print('swapping: ', n1, n2)
            swaps0 += 1


    swaps1 = 1
    nums1[-1], nums2[-1] = nums2[-1], nums1[-1],
    # check # swaps by changing 
    for i in range(len(nums1)-1):
        n1, n2 = nums1[i], nums2[i]
        if (n1 > nums1[-1] and n1 > nums2[-1]) or (n2 > nums1[-1] and n2 > nums2[-1]):
            return -1
        # n1 and n2 are greater than some max
        elif (n1 > nums1[-1] and n2 > nums1[-1] ) or (n1 > nums2[-1] and n2 > nums2[-1] ):
            return -1     
        elif n1 <= nums1[-1] and n2 <= nums2[-1]: 
            # print(n1, n2, nums1[-1], nums2[-1])
            continue
        elif (n1 > nums1[-1] and n1 <= nums2[-1]) or (n2 > nums2[-1] and n2 <= nums1[-1]): 
            swaps1 += 1


    # print("swaps0: ", swaps0, "swaps1: ", swaps1)
    return min(swaps0, swaps1 )

# nums1 = [1,2,7]
# nums2 = [4,5,3]


# nums1 = [2,3,4,5,9]
# nums2 = [8,8,4,4,4]

# nums1 = [1,5,4]
# nums2 = [2,5,3]

nums1 = [17,13,19,9,6,14]
nums2 = [17,14,15,1,19,19]

# nums1 = [5,6,4,9,0,17,10]
# nums2 = [7,2,8,2,3,3, 6]

print(minOperations(nums1, nums2))