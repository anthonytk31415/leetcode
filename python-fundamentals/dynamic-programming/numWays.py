# optimization on step 9 to save half the time, but still O(m*n) 

def numWays(steps, arrLen): 
    dpPrev = [0]*arrLen
    dpPrev[0] = 1
    dpCur = [0]*arrLen

    for _ in range(1, steps +1):
        for i in range(min(steps//2 + 1, arrLen)):
            dpCur[i] = dpPrev[i]
            if i > 0: dpCur[i] += dpPrev[i-1]
            if i < len(dpCur)-1: dpCur[i] += dpPrev[i+1]

        dpPrev, dpCur = dpCur, [0]*arrLen
    
    return (dpPrev[0]) % (10**9 +7)

steps = 438
arrLen = 315977

# steps = 4
# arrLen = 2
print(numWays(steps, arrLen))