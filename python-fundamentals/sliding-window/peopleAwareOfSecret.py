def peopleAwareOfSecret(n, delay, forget):

    curSum = 1
    arr = [0]*2*n
    arr[forget] = 1
    winLength = forget - delay + 1
    liveWindow = 0
    # print(arr, winLength, curSum, liveWindow)
    for i in range(1, n):
        curSum -= arr[i]
        liveWindow -= arr[i]
        liveWindow += arr[i + winLength - 1]
        # print(i, liveWindow, arr)
        curSum += liveWindow 
        arr[i + forget] = liveWindow

    # print(arr)
    return curSum % (10**9 + 7)


# n = 6
# delay = 2
# forget = 4

n = 4
delay = 1
forget = 3
print(peopleAwareOfSecret(n, delay, forget))