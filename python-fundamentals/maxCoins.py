# from collections import deque
def maxCoins(piles):
    piles.sort()
    res = 0
    for i in range(len(piles) - 2, len(piles)//3-1, -2):
        res += piles[i]
    return res


arr = [1,2,3,4,5,6,7,8,9]
print(maxCoins(arr))