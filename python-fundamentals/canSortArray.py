def canSortArray(nums):

    def countBits(num):
        countOnes = 0
        for x in num: 
            if x == "1": countOnes += 1
        return countOnes
    nums_b = [bin(x)[2:] for x in nums ]
    idx = {}
    for i in range(len(nums_b)):
        idx[nums_b[i]] = i
    
    nums_sb = [bin(x)[2:] for x in sorted(nums)]
    # print(nums  )
    # print(nums_b)
    # print(nums_sb)

    for i in range(len(nums)):
        j = idx[nums_sb[i]]
        u = min(i, j)
        v = max(i, j)
        while u < v: 
            if countBits(nums_b[u]) != countBits(nums_b[u + 1]): return False
            u += 1
    return True

# nums = [23, 24, 25, 26, 27, 1]
nums = [75,34,30]



# nums = [8,4,2,30,15]
# nums.sort()
# nums = [3,16,8,4,2]
# nums = [1,2,3,4,5]
# updated = [bin(x)[2:] for x in nums ]
# nums_b = [bin(x)[2:] for x in nums ]
# # print(updated)
# print(nums_b)
# nums_sorted = sorted(nums)
# nums_sb = [bin(x)[2:] for x in nums_sorted]
# print(nums_sb)
print(canSortArray(nums))


