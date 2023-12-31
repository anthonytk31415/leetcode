from math import inf
# i get a TLE. Why? This giant mess below is a O(d*n^2) implementation and unneeded. 

# def minDifficulty(jobDifficulty, d):
#     n = len(jobDifficulty)
#     if n < d: return - 1
#     if d == 1: return max(jobDifficulty)

#     memo = {}       
#     def f(d, i, j):
#         if (d,i,j) in memo: return memo[(d,i,j)]
#         res = inf
#         if d == 1: 
#             res =  max(jobDifficulty[i:j+1])
#         else:
#             for w in range(i, j+1):
#                 # condition: of width >= d-1 and bounds are good:
#                 if j - (w+1) + 1 >= d-1 and w+1 <= j: 
#                     curMin = f(1, i, w) + f(d-1, w+1, j)
#                     res = min(curMin, res)
#                 else: break 
#             for w in range(i, j+1):
#                 if w + -i + 1 >= d-1 and w+1 <= j: 
#                     curMin = f(d-1, i, w) + f(1, w+1, j)
#                     res = min(curMin, res)
#                 else: break
#             if res == inf: return 
#         memo[(d,i,j)] = res
#         return res

#     for k in range(1, d):
#         for i in range(n):
#             for j in range(i+1, n):
#                 if j - 1 + 1 >= k: f(k,i,j)
#     res = f(d, 0, n-1)
#     return res

def minDifficulty(jobDifficulty, d):
    arr = jobDifficulty
    n = len(arr)
    if n < d: return - 1
    if d == 1: return max(arr)
    dpPrev, dpCur, d1Memo = [-inf]*n, [-inf]*n, {}

    def d1(i,j):
        if (i,j) in d1Memo: return d1Memo[(i,j)]
        res = max(arr[i:j+1])
        d1Memo[(i,j)] = res
        return res

    for i in range(n):
        for j in range(i, n):
            cur = d1(i,j)
            if j == n-1:
                dpPrev[i] = cur

    def dfs(k, i):
        res = inf
        for j in range(i, len(arr)):
            if n-1 - (j+1) + 1 >= k-1 and j+1 < n: 
                curRes = d1(i, j) + dpPrev[j+1]
                res = min(res, curRes)
        dpCur[i] = res
        return res

    for k in range(2, d):
        for i in range(n):
            dfs(k, i)
        dpPrev, dpCur = dpCur, [-inf]*n

    return dfs(d, 0)

jobDifficulty = [5,7,2,6,3,1,9,8]
d = 4


# jobDifficulty = [6,5,4,3,2,1]
# d = 2
# jobDifficulty = [11,111,22,222,33,333,44,444]
# d = 6

# jobDifficulty = [9,9,9]
# d = 4

# jobDifficulty = [1,1,1]
# d = 3

jobDifficulty = [80,238,146,864,704,733,156,430,735,885,381,201,850,491,446,702,273,691,633,368,732,149,639,932,416,882,716,511,611,147,7,566,846,333,828,256,139,308,354,61,506,570,247,419,778,317,318,931,955,718,279,144,458,738,546,627,442,505,561,818,962,495,650,311,833,572,305,512,336,435,970,398,613,350,527,486,680,604,140,743,437,689,18,790,272,243,819,567,160,187,8,251,575,79,557,717,791,884,899,665,646,97,831,508,482,814,930,494,278,599,802,386,192,37,871,959,240,986,667,642,521,553,861,999,352,475,249,876,582,793,260,616,530,854,696,88,522,432,912,343,466,943,130,692,44,921,162,835,559,131,908,929,439,619,205,356,330,11,465,334,722,690,52,555,804,193,320,509,800,411,479,456,152,171,918,936,420,100,230,402,539,739,910,872,304]
d = 3
print(minDifficulty(jobDifficulty, d))