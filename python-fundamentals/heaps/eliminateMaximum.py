
# initiate a priority queue

from math import ceil 
def eliminateMaximum(dist, speed):
    times = [0 for _ in range(len(dist))]
    for i, iDist in enumerate(dist):
        iSpeed = speed[i]
        times[i] = ceil(iDist/iSpeed)

    times.sort()
    print(times)
    for i, time in enumerate(times):
        if time <= i: 
            return i
    return len(times)

dist = [1,3,4]
speed = [1,1,1]

# dist = [1,1,2,3]
# speed = [1,1,1,1]

# dist = [3,2,4]
# speed = [5,3,2]


print(eliminateMaximum(dist, speed))