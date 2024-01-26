# is it worth it to use a priority queue? 

# core trick: there are 6 options: 
# (1) add to get to y, sub to get to y, add to get to 5 multiple, sub to get to 5 multiple, 
# add to get to 11 multiple, sub to get to 11 multiple

# this is a BFS with priority queue implementation. 

# There's also a DFS with min applied and recursion solution that uses the same concept above. 
# there's also a DP solution and apparently you can prove by contradiction you never want to increase to get to some number below x. 




from heapq import heappush, heappop

def minimumOperationsToMakeEqual(x, y):
    queue = [(0, x)]
    
    while queue: 
        curOps, curVal = heappop(queue)
        if curVal == y: return int(curOps)
        if curVal < y: heappush(queue, (curOps + y-curVal, y))
        else: 
            heappush(queue, (curOps + abs(y-curVal), y))
            for x in [5, 11]:
                mod = curVal % x
                heappush(queue, (curOps + mod + 1, (curVal - mod )/ x))
                heappush(queue, (curOps + (x - mod) + 1, (curVal + (x - mod))/ x))

print(minimumOperationsToMakeEqual(x, y))
        



# x = 21
# y = 7
# x = 26
# y = 1

# x = 54
# y = 2

# x = 2
# y = 1
