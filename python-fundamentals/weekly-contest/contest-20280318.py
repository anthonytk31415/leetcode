# 10 min

def evenOddBit(n):
    even = 0
    odd = 0

    binary = bin(n)[2:]
    for i in range(len(binary)):
        idx = len(binary) - 1 - i
        if i %2 ==0 and binary[idx] == '1':
            even +=1
        if i %2 == 1 and binary[idx] == '1':
            odd +=1
        print(binary[idx])
    
    return [even,odd]

# print(evenOddBit(2))




def checkValidGrid(grid):

    knight_moves = [[-2,1], [-2,-1], [2,-1],[2,1,], [1,-2], [1,2], [-1, -2], [-1, 2]]
    visited = [[False for col in grid[0]] for row in grid]
    n = len(grid)-1
    end = len(grid) * len(grid[0])-1
    res = [False]
    def dfs(counter, i, j, knight_moves, visited, grid, end, n, res):
        visited[i][j] == True
        if counter == end: 
            res[0] = True
            return 
        
        for move in knight_moves:
            a,b = move
            u,v = i + a, j + b
            if 0 <= u <= n and 0 <= v <= n and not visited[u][v] and grid[u][v] == counter +1:
                dfs(counter + 1, u,v,knight_moves, visited, grid, end, n, res)

    dfs(0, 0,0,knight_moves, visited, grid, end, n, res)
    return res[0]

# grid = [[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]]
# grid = [[0,3,6],[5,8,1],[2,7,4]]

# print(checkValidGrid(grid))

from itertools import combinations 
# number of beautiful subsets
def beautifulSubsets(nums, k):
    singles = nums ## these will be added in the end
    combos = []
    for i in range(len(nums)+1):
        cur_combo = list(combinations(nums, i))
        combos.append(cur_combo)
    
    
    res = 0
    res += len(nums)
    if len(nums) == 1: 
        return res
    for i in range(2, len(nums)):
        cur_combo = combos[i]
        combos = list(combinations(cur_combo, i))
        combos_check = False
        for pair in combos: 
            x, y = pair
            if x + y == k: 
                combos_check = True
                break
        if combos_check == False: 
            res += 1
    return res

nums = [2,4,6]
k = 2

nums = [4,2,5,9,10,3]
1

print(beautifulSubsets(nums, k))



from collections import defaultdict, deque
from math import inf
def findSmallestInteger(nums, value):
    lookup = []
    for _ in range(value):
        lookup.append(deque())
    for i in range(len(nums)):
        mod_i = i % value
        lookup[mod_i].append(i)

    for x in nums: 
        x = x % value
        if lookup[x]:
            lookup[x].popleft()
    print(lookup)
    cur_min = inf
    for i in range(len(lookup)):
        if lookup[i]:
            cur = lookup[i].popleft()
            cur_min = min(cur_min, cur)


    if cur_min == inf: 
        return len(nums) 
    return cur_min

# nums = [1,-10,7,13,6,8]
# value = 5
# print(findSmallestInteger(nums, value))

# nums = [1,-10,7,13,6,8]
# value = 7
# print(findSmallestInteger(nums, value))

# nums = [1,1,2,2,3,3]
# value = 1
# nums = [3,0,3,2,4,2,1,1,0,4]
# value = 5
# print(findSmallestInteger(nums, value))



    # b_pairs = set()
    # nb_pairs = set()
    
    # ## do for pairs first then build off of pairs
    # for i in range(1, len(nums)-1):
    #     for j in range(i+1,len(nums)-1):
    #         pair = (nums[i], nums[j])
    #         if abs(nums[i] + nums[j]) != k: 
    #             b_pairs.add(pair)
    #         else: 
    #             nb_pairs.add(pair)
    