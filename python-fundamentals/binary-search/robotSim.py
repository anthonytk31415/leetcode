from collections import defaultdict
from bisect import bisect_right


def robotSim(commands, obstacles):

    def getDir(dIdx):
        # dirs = ['up', 'right', 'down', 'left']
        dirs = [[0,1], [1, 0], [0, -1], [-1, 0]]
        return dirs[dIdx % 4]

    obstacles = set([tuple([x, y]) for x, y in obstacles])
    x, y, overallMax, dIdx = 0, 0, 0, 0
    for c in commands: 
        if c == -2: 
            dIdx -= 1
        elif c == -1: 
            dIdx += 1
        else: 
            while c > 0: 
                deltaX, deltaY = getDir(dIdx)
                newX, newY = x + deltaX, y + deltaY
                if (newX, newY) in obstacles: break
                x, y = newX, newY
                c -=1
        overallMax = max(overallMax, (x - 0)**2 + (y - 0)**2)
    return overallMax

# commands = [4,-1,3]
# obstacles = []

# commands = [4,-1,4,-2,4]
# obstacles = [[2,4]]

commands = [6,-1,-1,6]
obstacles = []

print(robotSim(commands, obstacles))


# dirs = [[0,1], [1, 0], [0, -1], [-1, 0]]

# x, y = 1, 2                     # your x, y coordinate to start
# deltaX, deltaY = dirs[0]        # say you are facing up and will traverse upward
# newX, newY = x + deltaX, y + deltaY