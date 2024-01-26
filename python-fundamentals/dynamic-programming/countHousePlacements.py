def countHousePlacements(n):

    dpSinglePrev2 = [0] + [1] *n
    dpBothPrev2 = [0] + [1] *n
    dpTotalPrev2 = [0] + [1] *n

    dpSinglePrev = [0] + [1] *n
    dpBothPrev = [0]*(n+1)
    dpTotalPrev = [2*x for x in range(n+1)]

    dpSingleCur = [0]*(n+1)
    dpBothCur = [0]*(n+1)
    dpTotalCur = [0]*(n+1)

    for k in range(2, n+1):
        for i in range(1, n+1):
            # print(k, i)
            dpSingle = dpSinglePrev[i-1]
            if i -1 > 0: dpSingle += dpTotalPrev[i-2]
            dpSingleCur[i] = dpSingle

            dpBoth = 0 
            if k-2 == 0: dpBoth += 1
            else: dpBoth += dpTotalPrev2[i-2]
            dpBothCur[i] = dpBoth

            dpTotal = 2*dpSingleCur[i] + dpBothCur[i] + dpTotalCur[i-1]
            dpTotalCur[i] = dpTotal
    
        print(k, dpSingleCur, dpBothCur, dpTotalCur)

        dpSinglePrev2, dpSinglePrev, dpSingleCur = dpSinglePrev, dpSingleCur, [0]*(n+1)
        dpBothPrev2, dpBothPrev, dpBothCur = dpBothPrev, dpBothCur, [0]*(n+1)
        dpTotalPrev2, dpTotalPrev, dpTotalCur = dpTotalPrev, dpTotalCur, [0]*(n+1)

    return dpTotalPrev[-1]

n = 1

print(countHousePlacements(n))