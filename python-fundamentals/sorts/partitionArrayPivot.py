def pivotArray(nums, pivot):
    left = []
    right = []
    mid = []
    for x in nums: 
        if x < pivot: 
            left.append(x)
        if x == pivot: 
            mid.append(x)
        else: 
            right.append(x)
    return left + mid + right