from collections import deque


def getWinner1(arr, k):

    arrMax = max(arr)
    if k >= len(arr): 
        return arrMax

    curWinner = arr[0]

    queue = deque(arr[1:])
    counter = 0
    while queue: 
        if curWinner == arrMax: return curWinner
        curChallenger = queue.popleft()
        if curWinner > curChallenger: 
            counter += 1
        else: 
            curWinner, curChallenger = curChallenger, curWinner
            queue.append(curChallenger)
            counter = 1
        if counter == k: 
            return curWinner


# one optimization: you're always going to choose the larger element. so if you traverse your array 
# once, and you keep track of the larger element, all of the elements "behind" (to the left) of the current
# one will be smaller.
# 
#  

def getWinner(arr, k):
    winner = arr[0]
    wins = 0
    for i in range(1, len(arr)):
        challenger = arr[i]
        if winner <= challenger: 
            winner = challenger
            wins =0
        wins += 1
        if wins == k: 
            break 
    # If you get to the end of arr, and despite not hitting k, you foudn the largest 
    return winner



# arr = [2,1,3,5,4,6,7]
# k = 2


# arr = [1,25,35,42,68,70]
# k = 1
arr = [3,2,1]
k = 10

print(getWinner(arr, k))
        