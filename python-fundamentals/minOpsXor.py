from collections import deque
def minimumOperations(nums, start, goal):

    queue = deque()
    visited = set()
    queue.append([start, 0])
    while queue: 
        u, numOps = queue.popleft()
        if 0 <= u <= 1000: 
            for num in nums: 
                for v in [u + num, u - num, u ^ num]:
                    if v == goal: return numOps + 1
                    if v not in visited: 
                        queue.append([v, numOps + 1])
                        visited.add(v)
    return - 1

# nums = [2,4,12]
# start = 2
# goal = 12

nums = [3,5,7]
start = 0
goal = -4


nums = [2,8,16]
start = 0
goal = 1

print(minimumOperations(nums, start, goal))

# def xor(x, y):
#     z = x ^ y
#     print("x: {}, y: {}, x^y: {}, z: {}".format(bin(x), bin(y), bin(z), z))
#     return x ^ y


# z = xor(8, 4)
# print(z)

# z = xor(88, 23)
# print(z)