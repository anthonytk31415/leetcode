from collections import deque

def buildArray(target, n):

    stream = deque([i for i in range(1, n+1, 1)])
    operations = []
    idx = 0
    while idx < len(target):
        operations.append("Push")
        cur = stream.popleft()
        if cur == target[idx]:
            idx += 1
        else: 
            operations.append("Pop")

    return operations
        

# target = [1,3]
target = [1,2,3]
n = 3

print(buildArray(target, n))