def maxTurbulenceSize(arr):
    if len(arr) <= 1: 
        return len(arr)
    

    # prev: None, equal, pos, neg
    # cur: equal, pos, neg

    maxSize = 1
    prev = None
    cur = None
    dpPrev = 1
    dpCur = 0
    for i in range(1, len(arr)):
        # define cur
        if arr[i] == arr[i-1]:
            cur = "equal"
        elif arr[i] > arr[i-1]:
            cur = "pos"
        elif arr[i] < arr[i-1]:
            cur = "neg"
    
        if cur == "equal":
            dpCur = 1
        elif dpPrev == 1: 
            dpCur = dpPrev + 1
        elif (cur == "pos" and prev == "neg") or (cur == "neg" and prev == "pos"):
            dpCur = dpPrev + 1
        else: 
            dpCur = 2
        
        maxSize = max(maxSize, dpCur)
        prev, cur = cur, None
        dpPrev, dpCur = dpCur, 0
    return maxSize

arr = [1,2,3,4,5]


