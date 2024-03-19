# have a cooldown queue. when you consume something, put it in a queue sorted by time 

from heapq import heappush, heappop
from collections import Counter
def leastInterval(tasks, n):

    coolDown = []       # stored as (next available day, task, task num)
    nextAvailable = []  # stored as (tasknum, task)

    counter = Counter(tasks)
    for x in counter: 
        heappush(nextAvailable, (-counter[x], x))
    
    curDay = 0
    
    while coolDown or nextAvailable:
        curDay += 1
        print("cD: ", coolDown, "na: ", nextAvailable, "curday: ", curDay)

        while coolDown and coolDown[0][0] == curDay: 
            curAvail = heappop(coolDown)
            curAvailTask = curAvail[1]
            curTaskNum = curAvail[2]
            heappush(nextAvailable, (-curTaskNum, curAvailTask))

        if nextAvailable: 
            curTask = heappop(nextAvailable)
            numTask = -curTask[0]
            numTask -= 1
            task = curTask[1]

            if numTask > 0: 
                heappush(coolDown, (curDay + n + 1, task, numTask))



    
    return curDay

tasks = ["A","A","A","B","B","B"]
n = 2

tasks = ["A","C","A","B","D","B"]
n = 1


tasks = ["A","A","A", "B","B","B"]
n = 3
print(leastInterval(tasks, n))