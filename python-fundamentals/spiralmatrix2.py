def generateMatrix(n):
    res = [[0 for _ in range(n)] for _ in range(n)]

    imin, imax = 0, n-1
    jmin, jmax = 0, n-1
    i, j = 0, 0

    # go from at i, j to jmin > jmax; 
    # go at j = jmax, fro imin to imax; imin -=1
    # go at imax, from jmax to j; jmax -=1
    # go from imax to imin at jmin; 

    step = 0
    cur_idx = 1

    while cur_idx <= n**2:

        if step == 0: 
            for j in range(jmin, jmax+1):
                res[i][j] = cur_idx
                cur_idx +=1 
            # i +=1
            imin +=1
            step = 1

        elif step == 1: 
            for i in range(imin, imax+1):
                res[i][j] = cur_idx
                cur_idx +=1
            jmax -=1
            step = 2
        
        elif step == 2: 
            for j in range(jmax, jmin - 1, -1):
                res[i][j] = cur_idx
                cur_idx +=1
            imax -=1
            step = 3
        elif step == 3: 
            for i in range(imax, imin - 1, -1):
                res[i][j] = cur_idx
                cur_idx +=1
            jmin +=1
            step =0
    return res

print('res', generateMatrix(4))