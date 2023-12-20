from math import inf

def maxSumDivThree(nums):
    dpPrev, dpCur = [0]*3, [0]*3

    for i, num in enumerate(nums):
        for k in range(0, 3):
            mod = (dpPrev[k] + num) % 3
            dpCur[mod] = max(dpPrev[k] + num, dpPrev[mod], dpCur[mod])

        dpPrev, dpCur = dpCur, [x for x in dpCur]

    return dpPrev[0]

nums = [3,6,5,1,8]
[9, 0, 14]
[15, 10, 14]
print(maxSumDivThree(nums))