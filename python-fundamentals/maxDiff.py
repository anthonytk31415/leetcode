from math import inf
def maxDiff(num):

    arr = [int(x) for x in str(num)]

    def substitute(arr, x, y):
        res = [z for z in arr]
        for i in range(len(res)):
            if res[i] == x: res[i] = y
        
        res1 = 0
        for i in range(len(res)):
            res1 += res[i]
            if i != len(res) - 1: res1 *= 10
        return res1

    print("arr: ", arr)
    # create maxNum: 
    # if first char is not 9 then change it to 9
    # else: get to the first non-9, change that to 9
    x = -inf
    for char in arr: 
        if char != 9:
            x = char
            break
    
    maxNum = num
    if x != -inf: maxNum = substitute(arr, x, 9)
    print("maxnum: ", maxNum, x)


    # create minNum: 
    # if first char is not 1, change it to 1
    # if they're all 1, do  nothing
    # else: series of 1s on left followed by a non1: get to first non-1, change that to 0

    x = -inf
    minNum = num
    if arr[0] != 1: 
        x = arr[0]
        minNum = substitute(arr, x, 1)
    else: 
        for char in arr: 
            if char != 1 and char!= 0: 
                x = char
                break
        if x != -inf: minNum = substitute(arr, x, 0)
    
    print("minnum: ", minNum, x)
    return maxNum - minNum

num = 1101057
print(maxDiff(num))