print('contest - april 8, 2023')



# Q1: Check each diagonal number is a prime
# Q2: Prefix sum on the group of the same num
# Q3: Binary search on the answer
# Q4: Modified Dijkstra's using priority queue

## give the nums in diagonal

# sort them by largest
#start with largest and check if prime 

from functools import lru_cache

def getDiagonals(nums): 
    res = []
    for i in range(len(nums)):
        res.append(nums[i][i])
    for i in range(len(nums)):
        j = len(nums) - 1 - i
        if i != j: 
            res.append(nums[i][j])
    return res


# nums = [[1,2,3],[5,6,7],[9,10,11]]
# print(getDiagonals(nums))

def diagonalPrime(nums):
    diags = getDiagonals(nums)
    diags.sort(key=lambda x: -x)

    @lru_cache(None)
    def isPrime(n):
        if n == 1: 
            return False
        if n == 2: 
            return True
        for i in range(3, n):
            if n % i == 0: 
                return False
        return True

    for x in diags: 
        if isPrime(x):
            return x
    return 0    

# nums = [[1,2,3],[5,6,7],[9,10,11]]
# print(diagonalPrime(nums))


#make a hash table of key: val ==> num: list of indeces
#then iterate over length of nums:
# if hash(nums[i])'s length > 1: iterate

from collections import defaultdict

# TLE 

# from itertools import combinations
# create a hash table with list as the value, and append the index
# then run through the keys in the hash table. If the length of the list is > 1: 
# do some fancy sum stuff: 
# calculate the first sum at index 0 of the look = lookup[x]
# then for the next iteration k (1 through len(look)), 
#   you'd add to the sum found at index 0: 
#   delta = look[k] - look[k-1] each time there's an index < k, and subtract delta each time index >= k. 
#   then arr[look[k]] = sum


# Time: O(N)
# Space: O(N)

def distance(nums):
    lookup = defaultdict(list)
    arr = [0] * len(nums)
    for i, x in enumerate(nums):
        lookup[x].append(i)
    for x in lookup: 
        if len(lookup[x]) > 1: 
            look = lookup[x]
            curSum = sum([abs(look[0] - look[x]) for x in range(1, len(look))])
            arr[look[0]] = curSum
            for k in range(1, len(look)):
                delta = look[k] - look[k-1]
                curSum += delta * (k)
                curSum -= delta * (len(look) - k)
                arr[look[k]] = curSum
    return arr






# nums = [1,3,1,1,2]
# nums = [0,5,3]

# nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
# print(distance(nums))

from heapq import heappush, heappop
from math import inf

# def minimizeMax(nums, p):
#     minHeap = []
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             heappush(minHeap, (abs(nums[i] - nums[j]), i, j))

#     visited = set()
#     curMax = 0
#     e = 0
#     while e < p: 
#         dist, i, j = heappop(minHeap)
#         if i not in visited and j not in visited: 
#             curMax = max(dist, curMax)
#             visited.add(i)
#             visited.add(j)
#             e +=1
#     return curMax



# nums = [10,1,2,7,1,3]
# p = 2
# nums = [4,2,1,2]
# p = 1


# nums = [0,5,3,4]
# p = 0


    # nums.sort()
    # deltas = [None]*len(nums)
    # minHeap = []
    # for i in range(1, len(nums)):
    #     deltas[i] = nums[i] - nums[i-1] 
    #     heappush((deltas[i], i))
    
    # curMax = -inf
    # for _ in range(p):
        
# fucking TLE

# def minimizeMax(nums, p):

#     @lru_cache(None)
#     def minimizeMaxHelper(nums, p):
#         if p == 0: 
#             return 0
#         elif len(nums) == 2: 
#             return abs(nums[0] - nums[1])
#         else: 
#             res = []
#             for i in range(len(nums)):
#                 for j in range(i + 1, len(nums)):
#                     newNums = tuple(nums[:i] + nums[i+1:j] + nums[j+1:])
#                     res.append(max(abs(nums[i] - nums[j]), minimizeMaxHelper(newNums, p-1)))
#             return min(res)
    
#     return minimizeMaxHelper(tuple(nums), p)



def minimizeMax(nums, p):
    if p == 0: return 0
    nums.sort()
    left = 0
    right = nums[-1] - nums[0]
    while left < right: 
        i = 1
        counter = 0
        mid = (left + right) // 2
        while i < len(nums):
            if (nums[i] - nums[i-1]) <= mid: 
                counter +=1
                i +=2
            else: 
                i +=1

        # print(mid, left, right, counter, p)
        if counter >= p: 
            right = mid
        else: 
            left = mid + 1
    return left


# def minimizeMax(A, p):
#     A.sort()
#     n = len(A)
#     left, right = 0, A[-1] - A[0]
#     while left < right:
#         mid = (left + right) // 2
#         k = 0
#         i = 1
#         while i < n:
#             if A[i] - A[i - 1] <= mid:
#                 k += 1
#                 i += 1
#             i += 1
#         if k >= p:
#             right = mid
#         else:
#             left = mid + 1
#     return left


# nums = [3,11,4,3,5,7,4,4,5,5]
# p = 3
# nums = [75841,10836,90297,65300,2691,4222,31819,62366,74592,61726,2747,25749,82186,13526,68417,20213,51542,53629,48677,39515,1420,29980,82925,28030,48133,8712,18133,58186,90944,14106,58497,7113,22120,37507,8118,34489,55965,48887,18831,17644,77696,23889,705,28242,76776]
# p = 11



# nums = [10,1,2,7,1,3]
# p = 2

# # nums = [1,1,0,3]
# # p = 2
# print('min', minimizeMax(nums, p))



from collections import deque

def minimumVisitedCells(grid):
    m, n = len(grid), len(grid[0])
    queue = deque([(1,(0,0))])
    visited = set()
    visited.add((0,0))
    while queue: 
        curDist, coords = queue.popleft()
        (x,y) = coords
        if (x,y) == (m-1, n-1):
            return curDist
        maxi = grid[x][y] + x
        maxj = grid[x][y] + y
        for k in range(x+1, min(maxi + 1, m)):
            if (k, y) not in visited:
                if (k,y) == (m-1,n-1): return curDist + 1
                queue.append((curDist + 1, (k, y)))
                visited.add((k,y))
        for k in range(y+1, min(maxj + 1, n)):  
            if (x,k) not in visited:
                if (x,k) == (m-1,n-1): return curDist + 1
                queue.append((curDist + 1, (x, k)))
                visited.add((x,k))
    return -1

# grid = [[3,4,2,1],[4,2,3,1],[2,1,0,0],[2,4,0,0]]
grid = [[17,13,17,2],[14,3,2,1],[6,1,1,5],[16,16,9,9],[8,1,2,0]]

# grid = [[3,4,2,1],[4,2,1,1],[2,1,1,0],[3,4,1,0]]
# grid = [[2,1,0],[1,0,0]]
print(minimumVisitedCells(grid))