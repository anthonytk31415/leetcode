from collections import defaultdict


# hashmap implementation using prefix sums 
# first build an adjacency list for the num: [index1, index2, ...]
# then for each num, build a prefixSum. 
# then for eacn num and index in the adjacency, we calculate how much we have to increment 
# the other numbers to get to num. 
# we do the left side and right side trick. 

# O(n) Time and Space

def getDistances(arr):
    graph = defaultdict(list)
    prefix = defaultdict(list)

    for i, num in enumerate(arr):
        graph[num].append(i)
    
    for num in graph.keys():
        prefix[num] = [x for x in graph[num]]
        for i in range(1, len(prefix[num])):
            prefix[num][i] = prefix[num][i] + prefix[num][i-1]

    res = [0]*len(arr)
    for num in graph.keys():
        gnum = graph[num]
        n = len(graph[num])
        pfix = prefix[num]
        for i in range(len(gnum)):
            idx = gnum[i]
            curRes = 0
            if i == 0: curRes = abs(pfix[n-1] - (n-1 - 0 + 1)*gnum[i])
            elif i == n-1: curRes = abs(pfix[i] - (i+1)*gnum[i])
            else: curRes = abs(pfix[i-1]- (i)*gnum[i]) + abs(pfix[n-1] - pfix[i-1] - (n-1-i + 1) * gnum[i])
            res[idx] = curRes
    return res

arr = [2,1,3,1,2,3,3]
arr = [10,5,10,10]
print(getDistances(arr))