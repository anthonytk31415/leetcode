from collections import deque 

# Time: O(n*logn) for sorting neg and pos arrays
# Space: O(n) for keeping track of the array

# take neg and pos arrays sorted. 
# you want the largest benefit so smallest values first and largest values last. 
# Your solution will always contain the positives. 
# You add in the next smallest negative to the left of the positives only if the benefit > detriment. 
# The benefit for each "step" (step 0 is starting with positives, step 1 is adding the next smallest negative, etc.)
#   simply the sum of all integers in your current solution set. 
# you keep adding that next smallest integer until the detriment >= benefit. 

def maxSatisfaction(satisfaction):
    neg, pos = [], []

    for x in satisfaction:
        if x < 0: neg.append(x)
        else: pos.append(x)
    
    neg.sort()
    neg = deque(neg)
    pos.sort()
    curSum = 0
    benefit = sum(pos)
    for i, x in enumerate(pos):
        curSum += x*(i+1)
    while neg: 
        detriment = neg.pop()
        if benefit + detriment >0: 
            curSum = curSum + benefit + detriment
            benefit += detriment
        else: 
            break 
    return curSum

# satisfaction = [-1,-8,0,5,-9]


# satisfaction = [-1,-4,-5]
satisfaction = [4,3,2]

print(maxSatisfaction(satisfaction))