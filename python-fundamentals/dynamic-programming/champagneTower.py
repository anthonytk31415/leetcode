def champagneTower(poured, query_row, query_glass):
    # if poured == 0: return 0
    dpCur = []
    dpPrev = [poured]
    for i in range(0, query_row):
        for j in range(len(dpPrev) + 1):
            curRes = 0
            if j == 0: 
                curRes = .5*max(dpPrev[0]-1, 0)
            elif j == len(dpPrev):
                curRes = .5*max(dpPrev[-1] - 1, 0)
            else: 
                curRes = .5*(max(dpPrev[j] - 1, 0) + max(dpPrev[j-1] - 1, 0))
            dpCur.append(max(curRes,0))

        dpPrev, dpCur = dpCur, []
        
    return min(dpPrev[query_glass], 1)

# poured = 25
# query_row = 6
# query_glass = 1

poured = 0
query_row = 0
query_glass = 0


# poured = 100000009
# query_row = 33
# query_glass = 17

print(champagneTower(poured, query_row, query_glass))