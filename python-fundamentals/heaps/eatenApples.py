
# create a priority queue. for each i, insert the apples[i] into the queue and the days: [apples[i], days[i]]
# when you 

# 
from heapq import heappush, heappop

def eatenApples(apples, days):

    def popAndEat(curDay): 
        applesEaten = 0
        while queue and queue[0][0] <= curDay: 
            heappop(queue)
        if queue and queue[0][0] > curDay: 
            if queue[0][1] > 1: queue[0][1] -=1
            else: heappop(queue)
            applesEaten += 1
        return applesEaten

    queue = []
    eaten = 0
    curDay = 0

    for i in range(len(apples)):        
        heappush(queue, [days[i] + curDay ,apples[i]])
        eaten += popAndEat(curDay)
        curDay += 1

    while queue: 
        eaten += popAndEat(curDay)
        curDay += 1

    return eaten 


apples = [1,2,3,5,2]
days = [3,2,1,4,2]

# apples = [3,0,0,0,0,2]
# days = [3,0,0,0,0,2]

# apples = [1]
# days = [2]

print(eatenApples(apples, days))