from collections import defaultdict

# def prefers(x, u, y):
#     return friendPref[x][u] > friendPref[x][y]

# for a given x who is paired with y,
# there are CANDIDATES that have higher priority than y. 
# then for each CANDIDATE u, who is paired with v, 
# u has uCANDIDATES with higher priority than v. 
# if x is in uCANDIDATES, then x is unhappy. 

def unhappyFriends(n, preferences, pairs):
    friendPref = defaultdict(defaultdict)
    pairArr = [0]*n
    for i in range(len(preferences)):
        for j in range(len(preferences[i])):
            friendPref[i][preferences[i][j]] = j
    # print(friendPref)

    for a, b in pairs: 
        pairArr[a] = b
        pairArr[b] = a
    
    numUnhappy = 0
    for x in range(len(pairArr)):
        y = pairArr[x]
        yRank = friendPref[x][y]
        xCandidates = set(preferences[x][:yRank])
        for u in xCandidates: 
            v = pairArr[u]
            vRank = friendPref[u][v]
            uCandidates = set(preferences[u][:vRank])
            if x in uCandidates: 
                numUnhappy += 1
                break

    return numUnhappy

n = 4
preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]]
pairs = [[0, 1], [2, 3]]


n = 2
preferences = [[1], [0]]
pairs = [[1, 0]]

# n = 4
# preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]]
# pairs = [[1, 3], [0, 2]]

print(unhappyFriends(n, preferences, pairs))