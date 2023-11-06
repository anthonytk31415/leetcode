# print('hello world')
from collections import defaultdict

def distinctDifferenceArray(nums):
    num_distinct = [0]* len(nums)
    diff = [None] *len(nums)

    cur_set = defaultdict(int)
    # build distinct array 
    for i, x in enumerate(nums): 
        cur_set[x] +=1
        num_distinct[i] = len(cur_set)


    suffix = [0] * len(nums)

    # for each i, calculate the diff
    for i in range(len(num_distinct)):
        if cur_set[nums[i]] == 1: 
            del cur_set[nums[i]]
        else: 
            cur_set[nums[i]] -=1
        suffix[i] = len(cur_set)

    for i in range(len(diff)):
        diff[i] = num_distinct[i] - suffix[i]


    return diff


# nums = [3,2,3,4,2]
# nums = [1,2,3,4,5]
# print(distinctDifferenceArray(nums))


class FrequencyTracker:

    def __init__(self):
        self.counter = defaultdict(int) 
        self.freq = defaultdict(int)       

    def add(self, number: int) -> None:
        self.counter[number] +=1
        cur_freq = self.counter[number]
        ## update the freq
        if self.counter[number] == 1: 
            # in this condition, you just add cur length
            self.freq[cur_freq] +=1

        else: # remove the prev length; add the cur length
            if self.freq[cur_freq - 1] == 1: 
                del self.freq[cur_freq - 1]
            else: 
                self.freq[cur_freq - 1] -=1
            self.freq[cur_freq] +=1

    def deleteOne(self, number: int) -> None:
        if number in self.counter: 
            if self.counter[number] == 1:
                del self.counter[number]
                if self.freq[1] == 1: 
                    del self.freq[1]
                else: 
                    self.freq[1] -=1
            
            else: 
                self.counter[number] -=1
                cur_freq = self.counter[number]

                if self.freq[cur_freq + 1] == 1: 
                    del self.freq[cur_freq + 1]
                else: 
                    self.freq[cur_freq + 1] -=1

                self.freq[cur_freq] +=1


    def hasFrequency(self, frequency: int) -> bool:
        if frequency in self.freq: 
            return True
        else: 
            return False

# s = FrequencyTracker()
# print(s.add(3))
# print(s.add(3))
# print(s.add(3))
# print(s.add(2))
# print(s.counter, s.freq)

# print(s.deleteOne(2))
# print(s.deleteOne(2))
# print(s.deleteOne(3))

# print(s.counter, s.freq)

# print(s.hasFrequency(2))

# print(s.deleteOne(3))
# print(s.deleteOne(3))
# print(s.add(3))
# print(s.add(3))
# print(s.add(3))
# print(s.counter, s.freq)
# print(s.hasFrequency(2))
# print(s.hasFrequency(1))



def colorTheArray(n, queries):
    res = [0] * len(queries) 
    if n == 1: 
        return res
    
    nums = [0] * n

    # iterate across each query

    for query_idx, x in enumerate(queries):
        idx, color = x
        print(query_idx, idx, color)

        left_prev, right_prev = 0, 0
        if 0 <= idx - 1 and nums[idx-1] == nums[idx] and nums[idx] != 0: 
            left_prev = 1
        if idx + 1 < len(nums) and nums[idx + 1] == nums[idx] and nums[idx] != 0: 
            right_prev = 1

        nums[idx] = color
        left_cur, right_cur = 0, 0

        if 0 <= idx - 1 and nums[idx-1] == nums[idx] and nums[idx] != 0: 
            left_cur = 1
        if idx + 1 < len(nums) and nums[idx + 1] == nums[idx] and nums[idx] != 0: 
            right_cur = 1

        if query_idx != 0: 
            res[query_idx] = res[query_idx-1] + (left_cur + right_cur) - (left_prev + right_prev)

    return res

# n = 4
# queries = [[0,2],[1,2],[3,1],[1,1],[2,1]]

# n = 1
# queries = [[0,100000]]


# n = 4
# queries = [[0,1],[1,1],[2,1],[3,1],[4,1], [2,2], [3,2], [4,2]]

# n = 15
# queries = [[10,2],[12,1],[7,1],[11,1],[5,3],[14,3],[12,2],[14,3],[3,2],[13,3],[11,1],[2,2],[2,1],[4,2]]

# print(colorTheArray(n, queries))





# def minIncrements(n, cost):
#     res = 0
    
#     e = 0
#     level = 0
#     while e < n: 
#         curLevel = []    
#         for _ in range(2**level):
#             if e < n: 
#                 curLevel.append(cost[e])
#             e +=1
#         print(curLevel)
#         cur_max = max(curLevel)
#         for x in curLevel: 
#             res += max(0, cur_max - x)
#         level +=1 
#     return res


# dfs to get the max cost path

# then dfs from the root again
# carry the max cost value
# at each node: max_cost =  max_cost - cur.val 
# add to the node_increase max_cost - max sum of children
# then max_cost = max_cost - node_increase
# then for each child, recursively call with max cost


def minIncrements(n, cost):
    cost = [0] + cost ## so i = 1 is the first index 
    children_max = [0]*len(cost)
    res = [0]
    def dfs_max_cost(i):
        if i >= len(cost): 
            return 0
        else: 
            res = []
            res.append(dfs_max_cost(2*i))
            res.append(dfs_max_cost(2*i + 1))
            children_max[i] = max(res)
            return children_max[i] + cost[i]

    max_cost = dfs_max_cost(1)

    def dfs(i, max_cost):
        if i >= len(cost):
            return 
        max_cost -= cost[i]
        node_increase = max_cost - children_max[i]
        res[0] += node_increase
        max_cost -= node_increase

        dfs(2*i, max_cost)
        dfs(2*i + 1, max_cost)



    dfs(1, max_cost)
    return res[0]

# n = 7
# cost = [1,5,2,2,3,3,1]

# n = 12
# cost = [1, 2,3,4,5,6,7,8,9,10,11,12]





n = 15
cost = [764,1460,2664,764,2725,4556,5305,8829,5064,5929,7660,6321,4830,7055,3761]

print(minIncrements(n, cost))