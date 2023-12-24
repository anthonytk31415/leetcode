from collections import defaultdict
from math import inf 
from heapq import heappush, heappop

def minimumCost2(source, target, original, changed, cost):
    change = defaultdict(defaultdict)
    vertices = set()
    maxLengthOrig = -inf
    for i in range(len(original)):
        u = original[i]
        v = changed[i]
        vertices.add(u)
        vertices.add(v)
        dist = cost[i]
        if change[u] and v in change[u]:
            change[u][v] = min(change[u][v], dist)
        else: 
            change[u][v] = dist
        maxLengthOrig = max(maxLengthOrig, len(u))

    # cannot change to different lengths; dont want to go to the same vertex i == j
    for i in vertices: 
        for j in vertices:
            if len(i) != len(j): continue
            if i == j: continue
            if i != j and i not in change or j not in change[i]:
                change[i][j] = inf 

    # do floyd warshall but apply limitations 
    for k in vertices:
        for i in vertices:
            for j in vertices: 
                if i != j and j != k and i != k and len(i) == len(j) and len(j) == len(k): 
                    change[i][j] = min(change[i][j], change[i][k] + change[k][j])
                elif i + j == i + k + j :
                    if change[i][j] < change[i][k] + change[k][j]: change[i][j]
                    else: del change[i][j]

    # you'll have to split up the source to components of originals

    res = [inf]

    # print(change)

    queue = []
    heappush(queue, [0, 0])
    while queue: 
        i, curScore = heappop(queue)
        if i >= len(source):
            res[0] = min(res[0], curScore)
            if res[0] == inf: return -1
            return res[0]
        if source[i] == target[i]:
            heappush(queue, (i+1, curScore))
        for j in range(min(len(source), maxLengthOrig), -1, -1):
            u = source[i:i+j+1]
            v = target[i:i+j+1]
            if u != v and u in change and v in change[u]:                
                heappush(queue, (i + len(u), curScore + change[u][v]))
                
    return -1

    # for i in range(len(source)):    
    #     u = source[i]
    #     v = target[i]
    #     if u == v: continue
    #     if u not in change or v not in change[u]: return -1
    #     if change[u][v] == inf: 
    #         return -1
    #     res += change[u][v]

# source = "abcd"
# target = "acbe"
# original = ["a","b","c","c","e","d"]
# changed = ["b","c","b","e","b","e"]
# cost = [2,5,5,1,2,20]


# source = "abcdefgh"
# target = "acdeeghh" 
# original = ["bcd","fgh","thh"]
# changed = ["cde","thh","ghh"]
# cost = [1,3,5]

# source = "abcdefgh"
# target = "addddddd"
# original = ["bcd","defgh"]
# changed = ["ddd","ddddd"]
# cost = [100,1578]


# source = "acdcccbacdbcddbbcdbcaabdcdbaaacdbaddcdbacacacbbddcadcbcbaddbdcabadaddbccdaacccadcbdcdaccadacdadbadda"
# target = "acbbccbabaaaaccaacccaabaabcbdacbadcabacadaabcbbcdbadcbcbaddbdcabadaadbccdaacccadcbdcdaccadacdacbaddd"
# original = ["acdbcddbbcdb","dbabdaacbcbb","ccdaabbabcad","abdbddcabcdb","d","c","d","ddc","abb","cbd","add","bbb","cdc","dbd","dac","dbb","adb","a","b","bdcdbaa","dabdaab","dbabdad","dbaddcdbacaca","bccdbdbccabda","dabcbcddbbadc","d","a","c","b","ad"]
# changed = ["dbabdaacbcbb","ccdaabbabcad","abdbddcabcdb","abaaaaccaacc","c","d","a","abb","cbd","add","bbb","cdb","dbd","dac","dbb","adb","cbb","b","d","dabdaab","dbabdad","baabcbd","bccdbdbccabda","dabcbcddbbadc","badcabacadaab","a","c","b","d","ac"]
# cost = [91,38,44,93,77,58,100,86,96,100,48,90,98,87,62,82,95,60,83,36,60,100,82,75,85,42,93,89,93,94]

source = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
target = "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
original = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","aaaaaaaaaaa","aaaaaaaaaaaa","aaaaaaaaaaaaa","aaaaaaaaaaaaaa","aaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"]
changed = ["b","bb","bbb","bbbb","bbbbb","bbbbbb","bbbbbbb","bbbbbbbb","bbbbbbbbb","bbbbbbbbbb","bbbbbbbbbbb","bbbbbbbbbbbb","bbbbbbbbbbbbb","bbbbbbbbbbbbbb","bbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"]
cost = [54,41,62,4,68,100,60,32,64,58,57,8,67,85,20,83,80,71,6,82,88,97,29,29,78,53,32,11,64,10,93,32,32,99,57,35,35,46,84,91]

# 1323; 1577

# source = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# target = "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
# original = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","aaaaaaaaaaa","aaaaaaaaaaaa","aaaaaaaaaaaaa","aaaaaaaaaaaaaa","aaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"]
# changed = ["b","bb","bbb","bbbb","bbbbb","bbbbbb","bbbbbbb","bbbbbbbb","bbbbbbbbb","bbbbbbbbbb","bbbbbbbbbbb","bbbbbbbbbbbb","bbbbbbbbbbbbb","bbbbbbbbbbbbbb","bbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb","bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"]
# cost = [54,41,62,4,68,100,60,32,64,58,57,8,67,85,20,83,80,71,6,82,88,97,29,29,78,53,32,11,64,10,93,32,32,99,57,35,35,46,84,91]

# print(len(cost))

# source = "aaaa"
# target = "bbbb"
# original = ["a","c"]
# changed = ["c","b"]
# cost = [1,2]

# source = "abcd"
# target = "abce"
# original = ["a"]
# changed = ["e"]
# cost = [10000]

print(minimumCost2(source, target, original, changed, cost))