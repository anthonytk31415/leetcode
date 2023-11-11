# do breadth first search
from collections import deque
# def isReachableAtTime(sx, sy, fx, fy, t): 
#     visited = set([(sx, sy)])
#     queue = deque([(sx, sy)])
#     time = 0
#     while time <= t:         
#         curLength = len(queue)
#         for _ in range(curLength):
#             cur_x, cur_y = queue.popleft()
#             if cur_x == fx and cur_y == fy: return True
#             for next_x, next_y in [ (cur_x + 1, cur_y), (cur_x - 1, cur_y), (cur_x, cur_y + 1), (cur_x, cur_y - 1), 
#                                     (cur_x + 1, cur_y + 1), (cur_x - 1, cur_y + 1), (cur_x + 1, cur_y - 1), (cur_x - 1, cur_y - 1)]:
            
#                 if (next_x, next_y) not in visited: 
#                     visited.add((next_x, next_y))
#                     queue.append((next_x, next_y))
#         time += 1    
#     return False

def isReachableAtTime(sx, sy, fx, fy, t): 
    if sx == fx and sy == fy and t == 1: return False
    
    deltaX = abs(fx - sx)
    deltaY = abs(fy - sy)
    if deltaX <= t and deltaY <= t: return True

    return False



# sx = 2
# sy = 4
# fx = 7
# fy = 7
# t = 6
# print(isReachableAtTime(sx, sy, fx, fy, t))


# sx = 3
# sy = 1
# fx = 7
# fy = 3
# t = 3

# sx = 1
# sy = 1
# fx = 1
# fy = 3
# t = 2


sx = 1
sy = 4
fx = 1
fy = 2
t = 1

print(isReachableAtTime(sx, sy, fx, fy, t))