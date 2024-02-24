from collections import deque
from math import inf 
def determineDays(weights, capacity):
    d = deque(weights)
    numDays =  0
    curCapacity = 0
    while d: 
        curWeight = d.popleft()
        if curWeight > capacity: return inf
        # check of next is ok  
        if curCapacity + curWeight > capacity: 
            curCapacity = 0
            numDays += 1
        curCapacity += curWeight
    if curCapacity > 0: numDays += 1
    return numDays

weights = [1,2,3,4,5,6,7,8,9,10]
# print(determineDays(weights, 10))

def shipWithinDays(weights, days):


    def determineDays(weights, capacity):
        d = deque(weights)
        numDays =  0
        curCapacity = 0
        while d: 
            curWeight = d.popleft()
            if curWeight > capacity: return inf
            # check of next is ok  
            if curCapacity + curWeight > capacity: 
                curCapacity = 0
                numDays += 1
            curCapacity += curWeight
        if curCapacity > 0: numDays += 1
        return numDays
        
    sumWeights = sum(weights)
    left = 1
    right = sumWeights
    while left <= right: 
        mid = (left + right)// 2
        numDays = determineDays(weights, mid)
        
        if numDays > days: 
            left = mid + 1
        else: 
            right = mid - 1

    return left



# 15 + 15 + 25 = 55 / 15 --> 4

# weights = [1,2,3,4,5,6,7,8,9,10]
# days = 5

weights = [3,2,2,4,1,4]
days = 3


weights = [1,2,3,1,1]
days = 4
# sum = 16

print(shipWithinDays(weights, days))