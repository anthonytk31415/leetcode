def minOperations(nums1, nums2, k):
    if sum(nums1) != sum(nums2): return -1

    for i in range(len(nums1)):
        if nums1[i] % k != nums2[i] % k: return -1
    
    res = 0
    if nums1 == nums2: return res

    delta = 0
    for i in range(len(nums1)):
        delta += abs(nums1[i] - nums2[i])
    


    return int(delta / (2*k))



    # minus = 0 # points where nums1[minus] > nums2[minus] so you decrement minus
    # plus = 0  # points where n1[plus] < n2[plus] so you increment plus
    # while nums1 != nums2:

    #     while nums1[minus] <= nums2[minus]:
    #         minus += 1
    #     while nums1[plus] >= nums2[plus]:
    #         plus += 1
    #     nums1[minus] -= k
    #     nums1[plus] += k
    #     res += 1
    
    # return res




nums1 = [4,3,1,4]
nums2 = [1,3,7,1]
k = 3

print(minOperations(nums1, nums2, k))